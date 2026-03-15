#!/usr/bin/env python3
"""Generate an eval review viewer for skill output evaluation.

Usage:
    python eval-viewer/generate_review.py <workspace>/iteration-N \\
        --skill-name "my-skill" \\
        --benchmark <workspace>/iteration-N/benchmark.json \\
        [--previous-workspace <workspace>/iteration-N-1] \\
        [--static <output.html>]
"""

import argparse
import http.server
import json
import os
import threading
import webbrowser
from pathlib import Path


def load_iteration(iteration_dir: Path, configs=("with_skill",)):
    """Load eval data from an iteration directory."""
    evals = []
    for eval_dir in sorted(iteration_dir.iterdir()):
        if not eval_dir.is_dir() or eval_dir.name.startswith("."):
            continue
        meta_file = eval_dir / "eval_metadata.json"
        if not meta_file.exists():
            continue
        meta = json.loads(meta_file.read_text())
        runs = {}
        for config in eval_dir.iterdir():
            if not config.is_dir():
                continue
            outputs_dir = config / "outputs"
            output_files = {}
            if outputs_dir.exists():
                for f in outputs_dir.iterdir():
                    if f.is_file():
                        try:
                            output_files[f.name] = f.read_text(errors="replace")
                        except Exception:
                            output_files[f.name] = f"[binary file: {f.name}]"
            grading = None
            grading_file = config / "grading.json"
            if grading_file.exists():
                grading = json.loads(grading_file.read_text())
            runs[config.name] = {"outputs": output_files, "grading": grading}
        evals.append({"meta": meta, "runs": runs, "dir": eval_dir.name})
    return evals


def build_html(skill_name, evals, benchmark, prev_evals=None):
    benchmark_json = json.dumps(benchmark, indent=2) if benchmark else "null"
    evals_json = json.dumps(evals)
    prev_evals_json = json.dumps(prev_evals) if prev_evals else "null"

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Eval Review — {skill_name}</title>
<style>
  * {{ box-sizing: border-box; margin: 0; padding: 0; }}
  body {{ font-family: system-ui, sans-serif; background: #f5f5f5; color: #222; }}
  header {{ background: #1a1a2e; color: white; padding: 12px 24px; display: flex; align-items: center; gap: 16px; }}
  header h1 {{ font-size: 1rem; font-weight: 600; }}
  .tabs {{ display: flex; gap: 2px; margin-left: auto; }}
  .tab {{ padding: 6px 16px; border-radius: 4px; cursor: pointer; font-size: 0.875rem; background: rgba(255,255,255,0.1); color: white; border: none; }}
  .tab.active {{ background: white; color: #1a1a2e; font-weight: 600; }}
  .panel {{ display: none; padding: 24px; max-width: 960px; margin: 0 auto; }}
  .panel.active {{ display: block; }}
  .nav {{ display: flex; align-items: center; gap: 12px; margin-bottom: 20px; }}
  .nav button {{ padding: 6px 14px; border-radius: 4px; border: 1px solid #ccc; background: white; cursor: pointer; }}
  .nav button:hover {{ background: #f0f0f0; }}
  .counter {{ font-size: 0.875rem; color: #666; }}
  .eval-card {{ background: white; border-radius: 8px; padding: 20px; margin-bottom: 16px; box-shadow: 0 1px 3px rgba(0,0,0,0.1); }}
  .eval-card h3 {{ font-size: 0.75rem; text-transform: uppercase; letter-spacing: 0.05em; color: #888; margin-bottom: 8px; }}
  .prompt {{ background: #f8f8f8; border-left: 3px solid #1a1a2e; padding: 10px 14px; font-size: 0.9rem; border-radius: 0 4px 4px 0; }}
  .outputs {{ margin-top: 12px; }}
  .output-file {{ margin-top: 8px; }}
  .output-file summary {{ font-size: 0.8rem; color: #555; cursor: pointer; padding: 4px 0; }}
  .output-content {{ background: #1e1e1e; color: #d4d4d4; padding: 12px; border-radius: 4px; font-family: monospace; font-size: 0.8rem; white-space: pre-wrap; max-height: 300px; overflow-y: auto; margin-top: 6px; }}
  .grading {{ margin-top: 12px; }}
  .assertion {{ display: flex; gap: 8px; align-items: flex-start; padding: 6px 0; border-bottom: 1px solid #f0f0f0; font-size: 0.875rem; }}
  .assertion:last-child {{ border-bottom: none; }}
  .badge {{ padding: 2px 8px; border-radius: 10px; font-size: 0.75rem; font-weight: 600; flex-shrink: 0; }}
  .pass {{ background: #dcfce7; color: #166534; }}
  .fail {{ background: #fee2e2; color: #991b1b; }}
  .evidence {{ color: #666; font-size: 0.8rem; margin-top: 2px; }}
  textarea {{ width: 100%; padding: 10px; border: 1px solid #ccc; border-radius: 4px; font-size: 0.875rem; resize: vertical; min-height: 80px; margin-top: 8px; }}
  textarea:focus {{ outline: none; border-color: #1a1a2e; }}
  .submit-bar {{ position: sticky; bottom: 0; background: white; border-top: 1px solid #e0e0e0; padding: 12px 24px; display: flex; justify-content: flex-end; }}
  .submit-btn {{ background: #1a1a2e; color: white; border: none; padding: 10px 24px; border-radius: 6px; cursor: pointer; font-size: 0.9rem; font-weight: 600; }}
  .submit-btn:hover {{ background: #2d2d52; }}
  .benchmark-table {{ width: 100%; border-collapse: collapse; background: white; border-radius: 8px; overflow: hidden; box-shadow: 0 1px 3px rgba(0,0,0,0.1); }}
  .benchmark-table th {{ background: #1a1a2e; color: white; padding: 10px 14px; text-align: left; font-size: 0.8rem; }}
  .benchmark-table td {{ padding: 10px 14px; border-bottom: 1px solid #f0f0f0; font-size: 0.875rem; }}
  .benchmark-table tr:last-child td {{ border-bottom: none; }}
  .delta-positive {{ color: #166534; font-weight: 600; }}
  .delta-negative {{ color: #991b1b; font-weight: 600; }}
  .section-title {{ font-size: 1rem; font-weight: 600; margin: 20px 0 10px; }}
</style>
</head>
<body>
<header>
  <h1>Eval Review — {skill_name}</h1>
  <div class="tabs">
    <button class="tab active" onclick="showTab('outputs')">Outputs</button>
    <button class="tab" onclick="showTab('benchmark')">Benchmark</button>
  </div>
</header>

<div id="outputs" class="panel active">
  <div class="nav">
    <button onclick="navigate(-1)">← Prev</button>
    <span class="counter" id="counter"></span>
    <button onclick="navigate(1)">Next →</button>
  </div>
  <div id="eval-content"></div>
</div>

<div id="benchmark" class="panel">
  <div id="benchmark-content"></div>
</div>

<div class="submit-bar">
  <button class="submit-btn" onclick="submitAll()">Submit All Reviews</button>
</div>

<script>
const EVALS = {evals_json};
const PREV_EVALS = {prev_evals_json};
const BENCHMARK = {benchmark_json};
const feedback = {{}};
let current = 0;

function showTab(name) {{
  document.querySelectorAll('.panel').forEach(p => p.classList.remove('active'));
  document.querySelectorAll('.tab').forEach(t => t.classList.remove('active'));
  document.getElementById(name).classList.add('active');
  event.target.classList.add('active');
}}

function navigate(dir) {{
  saveFeedback();
  current = Math.max(0, Math.min(EVALS.length - 1, current + dir));
  render();
}}

function saveFeedback() {{
  const ta = document.getElementById('feedback-input');
  if (ta) {{
    const evalDir = EVALS[current].dir;
    feedback[evalDir + '-with_skill'] = ta.value;
  }}
}}

function render() {{
  const ev = EVALS[current];
  document.getElementById('counter').textContent = `${{current + 1}} / ${{EVALS.length}} — ${{ev.meta.eval_name || ev.dir}}`;

  const prevEv = PREV_EVALS ? PREV_EVALS.find(e => e.dir === ev.dir) : null;
  const run = ev.runs['with_skill'] || Object.values(ev.runs)[0] || {{}};
  const prevRun = prevEv ? (prevEv.runs['with_skill'] || Object.values(prevEv.runs)[0] || {{}}) : null;

  let html = `<div class="eval-card">
    <h3>Prompt</h3>
    <div class="prompt">${{ev.meta.prompt}}</div>
  </div>`;

  // Outputs
  const outputs = run.outputs || {{}};
  if (Object.keys(outputs).length) {{
    html += `<div class="eval-card"><h3>Output</h3><div class="outputs">`;
    for (const [name, content] of Object.entries(outputs)) {{
      html += `<details class="output-file" open><summary>📄 ${{name}}</summary>
        <div class="output-content">${{escapeHtml(content)}}</div></details>`;
    }}
    html += `</div></div>`;
  }} else {{
    html += `<div class="eval-card"><h3>Output</h3><p style="color:#999;font-size:0.875rem">No output files found.</p></div>`;
  }}

  // Previous output
  if (prevRun && Object.keys(prevRun.outputs || {{}}).length) {{
    html += `<div class="eval-card"><details><summary><strong>Previous Output</strong></summary><div class="outputs" style="margin-top:10px">`;
    for (const [name, content] of Object.entries(prevRun.outputs)) {{
      html += `<details class="output-file"><summary>📄 ${{name}}</summary>
        <div class="output-content">${{escapeHtml(content)}}</div></details>`;
    }}
    html += `</div></details></div>`;
  }}

  // Grading
  if (run.grading && run.grading.expectations) {{
    html += `<div class="eval-card"><details><summary><strong>Formal Grades</strong> — ${{run.grading.summary?.passed ?? '?'}}/${{run.grading.summary?.total ?? '?'}} passed</summary>
      <div class="grading" style="margin-top:10px">`;
    for (const e of run.grading.expectations) {{
      html += `<div class="assertion">
        <span class="badge ${{e.passed ? 'pass' : 'fail'}}">${{e.passed ? 'PASS' : 'FAIL'}}</span>
        <div><div>${{escapeHtml(e.text)}}</div><div class="evidence">${{escapeHtml(e.evidence || '')}}</div></div>
      </div>`;
    }}
    html += `</div></details></div>`;
  }}

  // Feedback
  const savedFeedback = feedback[ev.dir + '-with_skill'] || '';
  html += `<div class="eval-card"><h3>Your Feedback</h3>
    <textarea id="feedback-input" placeholder="What could be better? Leave blank if it looks good.">${{escapeHtml(savedFeedback)}}</textarea>
  </div>`;

  document.getElementById('eval-content').innerHTML = html;
}}

function buildBenchmark() {{
  if (!BENCHMARK) {{
    document.getElementById('benchmark-content').innerHTML = '<p style="color:#999;padding:20px">No benchmark data available.</p>';
    return;
  }}
  const summary = BENCHMARK.run_summary;
  let html = `<p class="section-title">Skill: ${{BENCHMARK.skill_name}}</p>
    <table class="benchmark-table">
      <thead><tr><th>Config</th><th>Pass Rate</th><th>Time (s)</th><th>Tokens</th></tr></thead><tbody>`;
  for (const [config, stats] of Object.entries(summary)) {{
    if (config === 'delta') continue;
    html += `<tr>
      <td><strong>${{config}}</strong></td>
      <td>${{(stats.pass_rate.mean * 100).toFixed(1)}}% ± ${{(stats.pass_rate.stddev * 100).toFixed(1)}}%</td>
      <td>${{stats.time_seconds.mean.toFixed(1)}} ± ${{stats.time_seconds.stddev.toFixed(1)}}</td>
      <td>${{Math.round(stats.tokens.mean)}} ± ${{Math.round(stats.tokens.stddev)}}</td>
    </tr>`;
  }}
  if (summary.delta) {{
    const d = summary.delta;
    const prClass = d.pass_rate > 0 ? 'delta-positive' : 'delta-negative';
    html += `<tr style="background:#f8f8f8">
      <td><em>delta</em></td>
      <td class="${{prClass}}">${{d.pass_rate > 0 ? '+' : ''}}${{(d.pass_rate * 100).toFixed(1)}}%</td>
      <td>${{d.time_seconds > 0 ? '+' : ''}}${{d.time_seconds.toFixed(1)}}s</td>
      <td>${{d.tokens > 0 ? '+' : ''}}${{Math.round(d.tokens)}}</td>
    </tr>`;
  }}
  html += `</tbody></table>`;
  document.getElementById('benchmark-content').innerHTML = html;
}}

function submitAll() {{
  saveFeedback();
  const reviews = Object.entries(feedback).map(([run_id, fb]) => ({{
    run_id, feedback: fb, timestamp: new Date().toISOString()
  }}));
  const blob = new Blob([JSON.stringify({{reviews, status: 'complete'}}, null, 2)], {{type: 'application/json'}});
  const a = document.createElement('a');
  a.href = URL.createObjectURL(blob);
  a.download = 'feedback.json';
  a.click();
}}

function escapeHtml(str) {{
  return String(str).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;');
}}

document.addEventListener('keydown', e => {{
  if (e.key === 'ArrowLeft') navigate(-1);
  if (e.key === 'ArrowRight') navigate(1);
}});

render();
buildBenchmark();
</script>
</body>
</html>"""


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("iteration_dir", type=Path)
    parser.add_argument("--skill-name", default="Skill")
    parser.add_argument("--benchmark", type=Path)
    parser.add_argument("--previous-workspace", type=Path)
    parser.add_argument("--static", type=Path, help="Write static HTML to this path instead of serving")
    args = parser.parse_args()

    evals = load_iteration(args.iteration_dir)
    prev_evals = load_iteration(args.previous_workspace) if args.previous_workspace else None
    benchmark = json.loads(args.benchmark.read_text()) if args.benchmark and args.benchmark.exists() else None

    html = build_html(args.skill_name, evals, benchmark, prev_evals)

    if args.static:
        args.static.write_text(html)
        print(f"Wrote static viewer to {args.static}")
        return

    # Serve locally
    import io
    html_bytes = html.encode()
    port = 8765

    class Handler(http.server.BaseHTTPRequestHandler):
        def do_GET(self):
            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.end_headers()
            self.wfile.write(html_bytes)

        def log_message(self, fmt, *args):
            pass  # suppress request logs

    server = http.server.HTTPServer(("localhost", port), Handler)
    url = f"http://localhost:{port}"
    print(f"Eval viewer running at {url}")
    print("Press Ctrl+C to stop.")
    threading.Thread(target=lambda: webbrowser.open(url), daemon=True).start()
    server.serve_forever()


if __name__ == "__main__":
    main()