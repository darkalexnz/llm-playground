#!/usr/bin/env python3
"""Aggregate grading results into benchmark.json and benchmark.md.

Usage:
    python -m scripts.aggregate_benchmark <workspace>/iteration-N --skill-name <name>
"""

import argparse
import json
import math
from pathlib import Path


def mean_stddev(values):
    if not values:
        return {"mean": 0, "stddev": 0}
    m = sum(values) / len(values)
    s = math.sqrt(sum((v - m) ** 2 for v in values) / max(len(values) - 1, 1)) if len(values) > 1 else 0
    return {"mean": round(m, 4), "stddev": round(s, 4)}


def collect_run_data(run_dir: Path):
    grading_file = run_dir / "grading.json"
    timing_file = run_dir / "timing.json"
    pass_rates, time_seconds, tokens = [], [], []

    if grading_file.exists():
        grading = json.loads(grading_file.read_text())
        expectations = grading.get("expectations", grading.get("assertion_results", []))
        if expectations:
            passed = sum(1 for e in expectations if e.get("passed"))
            pass_rates.append(passed / len(expectations))

    if timing_file.exists():
        timing = json.loads(timing_file.read_text())
        if "duration_ms" in timing:
            time_seconds.append(timing["duration_ms"] / 1000)
        if "total_tokens" in timing:
            tokens.append(timing["total_tokens"])

    return pass_rates, time_seconds, tokens


def aggregate(iteration_dir: Path, skill_name: str):
    configs = {}

    for eval_dir in sorted(iteration_dir.iterdir()):
        if not eval_dir.is_dir() or eval_dir.name.startswith("."):
            continue
        for run_dir in sorted(eval_dir.iterdir()):
            if not run_dir.is_dir():
                continue
            config = run_dir.name
            if config not in configs:
                configs[config] = {"pass_rates": [], "time_seconds": [], "tokens": []}
            pr, ts, tk = collect_run_data(run_dir)
            configs[config]["pass_rates"].extend(pr)
            configs[config]["time_seconds"].extend(ts)
            configs[config]["tokens"].extend(tk)

    # Build summary — with_skill first, then baseline
    ordered_configs = sorted(configs.keys(), key=lambda c: (0 if c == "with_skill" else 1))
    summary = {c: {
        "pass_rate": mean_stddev(configs[c]["pass_rates"]),
        "time_seconds": mean_stddev(configs[c]["time_seconds"]),
        "tokens": mean_stddev(configs[c]["tokens"]),
    } for c in ordered_configs}

    base = "without_skill" if "without_skill" in summary else "old_skill"
    if "with_skill" in summary and base in summary:
        summary["delta"] = {
            "pass_rate": round(summary["with_skill"]["pass_rate"]["mean"] - summary[base]["pass_rate"]["mean"], 4),
            "time_seconds": round(summary["with_skill"]["time_seconds"]["mean"] - summary[base]["time_seconds"]["mean"], 4),
            "tokens": round(summary["with_skill"]["tokens"]["mean"] - summary[base]["tokens"]["mean"], 4),
        }

    benchmark = {"skill_name": skill_name, "run_summary": summary}

    out_json = iteration_dir / "benchmark.json"
    out_json.write_text(json.dumps(benchmark, indent=2))

    lines = [f"# Benchmark: {skill_name}\n"]
    for config, stats in summary.items():
        if config == "delta":
            continue
        lines.append(f"## {config}")
        lines.append(f"- Pass rate: {stats['pass_rate']['mean']:.1%} ± {stats['pass_rate']['stddev']:.1%}")
        lines.append(f"- Time: {stats['time_seconds']['mean']:.1f}s ± {stats['time_seconds']['stddev']:.1f}s")
        lines.append(f"- Tokens: {stats['tokens']['mean']:.0f} ± {stats['tokens']['stddev']:.0f}\n")
    if "delta" in summary:
        d = summary["delta"]
        lines.append("## Delta (with_skill vs baseline)")
        lines.append(f"- Pass rate: {d['pass_rate']:+.1%}")
        lines.append(f"- Time: {d['time_seconds']:+.1f}s")
        lines.append(f"- Tokens: {d['tokens']:+.0f}")

    out_md = iteration_dir / "benchmark.md"
    out_md.write_text("\n".join(lines) + "\n")

    print(f"Wrote {out_json}")
    print(f"Wrote {out_md}")
    return benchmark


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("iteration_dir", type=Path)
    parser.add_argument("--skill-name", default="unknown")
    args = parser.parse_args()
    aggregate(args.iteration_dir, args.skill_name)
