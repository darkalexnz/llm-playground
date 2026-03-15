#!/usr/bin/env python3
"""Description optimization loop for skill triggering accuracy.

Usage:
    python -m scripts.run_loop \
        --eval-set <path-to-trigger-eval.json> \
        --skill-path <path-to-skill> \
        --model <model-id> \
        --max-iterations 5 \
        --verbose

Outputs:
    <skill-path>/optimization_results.json  — all iterations + best_description
    Opens an HTML report in the browser when done.
"""

import argparse
import json
import os
import random
import re
import subprocess
import sys
import tempfile
import webbrowser
from pathlib import Path


# ── helpers ──────────────────────────────────────────────────────────────────

def load_eval_set(path: Path) -> list[dict]:
    data = json.loads(path.read_text())
    if isinstance(data, list):
        return data
    # support {"evals": [...]} wrapper
    return data.get("evals", data)


def split_eval_set(evals: list[dict], seed: int = 42) -> tuple[list, list]:
    """60% train / 40% test, seeded."""
    items = evals[:]
    random.seed(seed)
    random.shuffle(items)
    split = int(len(items) * 0.6)
    return items[:split], items[split:]


def read_skill_name(skill_path: Path) -> str:
    skill_md = skill_path / "SKILL.md"
    text = skill_md.read_text()
    m = re.search(r"^name:\s*(.+)$", text, re.MULTILINE)
    return m.group(1).strip() if m else skill_path.name


def test_trigger(query: str, skill_name: str, description: str, model: str, runs: int = 3) -> bool:
    """Ask Claude whether it would trigger the skill for this query. Majority vote."""
    system = (
        f"You have one available skill:\n"
        f"  [{skill_name}]: {description}\n\n"
        "A user has sent you a message. Reply with exactly one word: "
        "TRIGGER if you would invoke this skill to help with the request, "
        "or SKIP if you would handle it without the skill."
    )
    votes = []
    for _ in range(runs):
        try:
            result = subprocess.run(
                ["claude", "-p", query, "--model", model],
                input=system,
                capture_output=True,
                text=True,
                timeout=30,
                env={**os.environ, "ANTHROPIC_SYSTEM_PROMPT": system},
            )
            out = result.stdout.strip().upper()
            votes.append("TRIGGER" in out)
        except Exception:
            votes.append(False)
    return votes.count(True) > len(votes) / 2


def score_description(evals: list[dict], skill_name: str, description: str, model: str, verbose: bool) -> float:
    correct = 0
    for item in evals:
        query = item.get("query", item.get("prompt", ""))
        should = item.get("should_trigger", True)
        triggered = test_trigger(query, skill_name, description, model)
        if triggered == should:
            correct += 1
        if verbose:
            mark = "✓" if triggered == should else "✗"
            print(f"  {mark} should={'Y' if should else 'N'} got={'Y' if triggered else 'N'} | {query[:60]}")
    return correct / len(evals) if evals else 0.0


def propose_improved_description(
    skill_name: str,
    current_description: str,
    failures: list[dict],
    model: str,
) -> str:
    """Ask Claude to propose a better description based on failures."""
    failure_lines = "\n".join(
        f"- Query: {f['query']!r} | Should trigger: {f['should_trigger']} | Got: {f['triggered']}"
        for f in failures
    )
    prompt = (
        f"You are improving the description field of a skill called '{skill_name}'.\n\n"
        f"Current description:\n{current_description}\n\n"
        f"The description is used to decide whether to invoke the skill. "
        f"The following queries were mis-classified:\n{failure_lines}\n\n"
        "Write an improved description that fixes these failures. "
        "Return ONLY the new description text, nothing else."
    )
    try:
        result = subprocess.run(
            ["claude", "-p", prompt, "--model", model],
            capture_output=True, text=True, timeout=60,
        )
        return result.stdout.strip()
    except Exception as e:
        print(f"  Warning: could not get improved description: {e}", file=sys.stderr)
        return current_description


def generate_html_report(results: list[dict], skill_name: str) -> str:
    rows = ""
    for r in results:
        rows += (
            f"<tr><td>{r['iteration']}</td>"
            f"<td>{r['train_score']:.1%}</td>"
            f"<td>{r['test_score']:.1%}</td>"
            f"<td style='font-size:0.85em;word-break:break-word'>{r['description']}</td></tr>\n"
        )
    best = max(results, key=lambda x: x["test_score"])
    return f"""<!DOCTYPE html>
<html><head><meta charset="utf-8">
<title>Description Optimization: {skill_name}</title>
<style>
  body {{ font-family: system-ui, sans-serif; max-width: 960px; margin: 2rem auto; padding: 0 1rem; }}
  h1 {{ font-size: 1.4rem; }}
  table {{ border-collapse: collapse; width: 100%; }}
  th, td {{ border: 1px solid #ddd; padding: 0.5rem 0.75rem; text-align: left; vertical-align: top; }}
  th {{ background: #f5f5f5; }}
  .best {{ background: #e6ffe6; }}
  .best-desc {{ background: #f0fff0; padding: 1rem; border: 1px solid #aaa; margin-top: 1rem; }}
</style></head>
<body>
<h1>Description Optimization: {skill_name}</h1>
<table>
  <thead><tr><th>#</th><th>Train</th><th>Test</th><th>Description</th></tr></thead>
  <tbody>{rows}</tbody>
</table>
<div class="best-desc">
  <strong>Best description (iteration {best['iteration']}, test {best['test_score']:.1%}):</strong><br>
  <pre style="white-space:pre-wrap">{best['description']}</pre>
</div>
</body></html>"""


# ── main ─────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--eval-set", required=True, type=Path)
    parser.add_argument("--skill-path", required=True, type=Path)
    parser.add_argument("--model", default="claude-sonnet-4-6")
    parser.add_argument("--max-iterations", type=int, default=5)
    parser.add_argument("--verbose", action="store_true")
    args = parser.parse_args()

    evals = load_eval_set(args.eval_set)
    train, test = split_eval_set(evals)
    skill_name = read_skill_name(args.skill_path)

    # Read current description
    skill_md = args.skill_path / "SKILL.md"
    text = skill_md.read_text()
    m = re.search(r"^description:\s*(.+)$", text, re.MULTILINE)
    description = m.group(1).strip() if m else ""

    print(f"Skill: {skill_name}")
    print(f"Eval set: {len(evals)} queries ({len(train)} train / {len(test)} test)")
    print(f"Model: {args.model}\n")

    results = []

    for i in range(1, args.max_iterations + 1):
        print(f"── Iteration {i} ──────────────────────────────────")
        if args.verbose:
            print("  [train]")
        train_score = score_description(train, skill_name, description, args.model, args.verbose)
        if args.verbose:
            print("  [test]")
        test_score = score_description(test, skill_name, description, args.model, args.verbose)
        print(f"  train={train_score:.1%}  test={test_score:.1%}")

        results.append({
            "iteration": i,
            "description": description,
            "train_score": train_score,
            "test_score": test_score,
        })

        if i == args.max_iterations:
            break

        # Collect failures from train set to guide improvement
        failures = []
        for item in train:
            query = item.get("query", item.get("prompt", ""))
            should = item.get("should_trigger", True)
            triggered = test_trigger(query, skill_name, description, args.model)
            if triggered != should:
                failures.append({"query": query, "should_trigger": should, "triggered": triggered})

        if not failures:
            print("  No failures on train set — stopping early.")
            break

        print(f"  {len(failures)} failures → requesting improved description...")
        description = propose_improved_description(skill_name, description, failures, args.model)

    # Select best by test score
    best = max(results, key=lambda x: x["test_score"])
    output = {"skill_name": skill_name, "iterations": results, "best_description": best["description"]}

    out_path = args.skill_path / "optimization_results.json"
    out_path.write_text(json.dumps(output, indent=2))
    print(f"\nResults written to {out_path}")
    print(f"Best description (iteration {best['iteration']}, test {best['test_score']:.1%}):")
    print(best["description"])

    # HTML report
    html = generate_html_report(results, skill_name)
    with tempfile.NamedTemporaryFile("w", suffix=".html", delete=False) as f:
        f.write(html)
        webbrowser.open(f"file://{f.name}")

    print(json.dumps({"best_description": best["description"]}))


if __name__ == "__main__":
    main()
