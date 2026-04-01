const $ = (selector) => document.querySelector(selector);

const summaryOutput = $("#summary-output");
const commandsList = $("#commands-list");
const toolsList = $("#tools-list");
const routeResults = $("#route-results");
const agenticResults = $("#agentic-results");
const commandCount = $("#command-count");
const toolCount = $("#tool-count");
const pythonFiles = $("#python-files");

function esc(value) {
  return String(value)
    .replaceAll("&", "&amp;")
    .replaceAll("<", "&lt;")
    .replaceAll(">", "&gt;");
}

async function fetchJson(url) {
  const response = await fetch(url);
  if (!response.ok) {
    throw new Error(`Request failed: ${response.status}`);
  }
  return response.json();
}

function renderEntries(target, entries) {
  if (!entries.length) {
    target.innerHTML = `<li>No results</li>`;
    return;
  }
  target.innerHTML = entries
    .map(
      (entry) => `
      <li>
        <strong>${esc(entry.name)}</strong>
        <div class="mono">${esc(entry.source_hint)}</div>
      </li>`
    )
    .join("");
}

async function loadManifest() {
  const data = await fetchJson("/api/manifest");
  pythonFiles.textContent = data.total_python_files;
}

async function loadSummary() {
  const data = await fetchJson("/api/summary");
  summaryOutput.textContent = data.markdown;
}

async function loadCommands() {
  const q = $("#command-query").value.trim();
  const params = new URLSearchParams({ limit: "12" });
  if (q) params.set("query", q);
  const data = await fetchJson(`/api/commands?${params.toString()}`);
  commandCount.textContent = data.total;
  renderEntries(commandsList, data.entries);
}

async function loadTools() {
  const q = $("#tool-query").value.trim();
  const params = new URLSearchParams({ limit: "12" });
  if (q) params.set("query", q);
  const data = await fetchJson(`/api/tools?${params.toString()}`);
  toolCount.textContent = data.total;
  renderEntries(toolsList, data.entries);
}

async function routePrompt(event) {
  event.preventDefault();
  const prompt = $("#route-prompt").value.trim();
  const limit = $("#route-limit").value || "5";
  if (!prompt) {
    routeResults.innerHTML = `<div class="result-item">Prompt is required.</div>`;
    return;
  }
  const params = new URLSearchParams({ prompt, limit });
  const data = await fetchJson(`/api/route?${params.toString()}`);
  if (!data.matches.length) {
    routeResults.innerHTML = `<div class="result-item">No matches found.</div>`;
    return;
  }
  routeResults.innerHTML = data.matches
    .map(
      (match) => `
      <div class="result-item">
        <strong>${esc(match.kind)} :: ${esc(match.name)}</strong>
        <div>score: ${esc(match.score)}</div>
        <div class="mono">${esc(match.source_hint)}</div>
      </div>`
    )
    .join("");
}

async function runAgenticDemo(event) {
  event.preventDefault();
  const prompts = $("#agentic-prompts")
    .value.split("\n")
    .map((line) => line.trim())
    .filter(Boolean);
  if (prompts.length < 2) {
    agenticResults.innerHTML = `<div class="result-item">Provide at least two prompts (one per line).</div>`;
    return;
  }
  if (prompts.length > 5) {
    agenticResults.innerHTML = `<div class="result-item">Use at most five prompts.</div>`;
    return;
  }
  const routeLimit = Number($("#agentic-limit").value || "5");
  const response = await fetch("/api/agentic-demo", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ prompts, route_limit: routeLimit }),
  });
  if (!response.ok) {
    agenticResults.innerHTML = `<div class="result-item">Agentic request failed: ${response.status}</div>`;
    return;
  }
  const data = await response.json();
  const workerCards = data.workers
    .map(
      (worker) => `
      <div class="result-item">
        <strong>${esc(worker.agent_id)} (${esc(worker.role)})</strong>
        <p>commands=${esc(worker.matched_commands.length)} tools=${esc(worker.matched_tools.length)} stop=${esc(worker.stop_reason)} duration_ms=${esc(worker.duration_ms)}</p>
        <pre>${esc(worker.output)}</pre>
      </div>`
    )
    .join("");
  agenticResults.innerHTML = `
    <div class="result-item">
      <strong>Main Orchestrator</strong>
      <p>workers=${esc(data.worker_count)} total_duration_ms=${esc(data.total_duration_ms)}</p>
      <pre>${esc(data.orchestrator_summary)}</pre>
    </div>
    ${workerCards}
  `;
}

async function init() {
  try {
    await Promise.all([loadManifest(), loadSummary(), loadCommands(), loadTools()]);
  } catch (error) {
    summaryOutput.textContent = `Failed to load dashboard data: ${error.message}`;
  }
}

$("#refresh-commands").addEventListener("click", loadCommands);
$("#refresh-tools").addEventListener("click", loadTools);
$("#route-form").addEventListener("submit", routePrompt);
$("#agentic-form").addEventListener("submit", runAgenticDemo);
$("#command-query").addEventListener("keydown", (event) => {
  if (event.key === "Enter") {
    event.preventDefault();
    loadCommands();
  }
});
$("#tool-query").addEventListener("keydown", (event) => {
  if (event.key === "Enter") {
    event.preventDefault();
    loadTools();
  }
});

init();
