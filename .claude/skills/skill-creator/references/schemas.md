# Schemas Reference

JSON structures used across the skill evaluation system.

---

## evals.json

Defines test cases for a skill. Lives at `evals/evals.json` inside the skill directory.

```json
{
  "skill_name": "my-skill",
  "evals": [
    {
      "id": 1,
      "prompt": "Realistic user message — what someone would actually type",
      "expected_output": "Human-readable description of what success looks like",
      "files": ["evals/files/input.csv"],
      "assertions": [
        "The output contains a file named report.pdf",
        "The summary section is present and non-empty",
        "All 5 input rows are represented in the output"
      ]
    }
  ]
}
```

- `files`: paths relative to the skill directory; omit or use `[]` if no input files
- `assertions`: add after the first run while baselines are executing; leave `[]` initially

---

## eval_metadata.json

Written per eval directory during a run. Lives at `<workspace>/iteration-N/<eval-name>/eval_metadata.json`.

```json
{
  "eval_id": 1,
  "eval_name": "descriptive-name-for-this-eval",
  "prompt": "The user's task prompt",
  "assertions": [
    "The output contains a file named report.pdf",
    "The summary section is present and non-empty"
  ]
}
```

---

## grading.json

Output of the grader. Lives at `<workspace>/iteration-N/<eval-name>/<run-config>/grading.json`.

```json
{
  "expectations": [
    {
      "text": "The output contains a file named report.pdf",
      "passed": true,
      "evidence": "Found report.pdf (12KB) in outputs/"
    },
    {
      "text": "The summary section is present and non-empty",
      "passed": false,
      "evidence": "report.pdf exists but contains no 'Summary' heading"
    }
  ],
  "summary": {
    "passed": 1,
    "failed": 1,
    "total": 2,
    "pass_rate": 0.5
  }
}
```

**Field names are strict:** `text`, `passed`, `evidence` — the viewer breaks if you use alternatives.

---

## timing.json

Captured from subagent task completion notification. Lives alongside `grading.json`.

```json
{
  "total_tokens": 84852,
  "duration_ms": 23332,
  "total_duration_seconds": 23.3
}
```

---

## benchmark.json

Aggregated output of `scripts/aggregate_benchmark.py`. Lives at `<workspace>/iteration-N/benchmark.json`.

```json
{
  "skill_name": "my-skill",
  "run_summary": {
    "with_skill": {
      "pass_rate": {"mean": 0.83, "stddev": 0.06},
      "time_seconds": {"mean": 45.0, "stddev": 12.0},
      "tokens": {"mean": 3800, "stddev": 400}
    },
    "without_skill": {
      "pass_rate": {"mean": 0.33, "stddev": 0.10},
      "time_seconds": {"mean": 32.0, "stddev": 8.0},
      "tokens": {"mean": 2100, "stddev": 300}
    },
    "delta": {
      "pass_rate": 0.5,
      "time_seconds": 13.0,
      "tokens": 1700
    }
  }
}
```

- List `with_skill` before its baseline counterpart
- `delta` = with_skill minus baseline (positive = skill costs more time/tokens, positive pass_rate delta = skill is better)
- For improving an existing skill, baseline config is `old_skill` instead of `without_skill`

---

## feedback.json

Downloaded from the eval viewer when the user clicks "Submit All Reviews".

```json
{
  "reviews": [
    {
      "run_id": "eval-descriptive-name-with_skill",
      "feedback": "The chart is missing axis labels",
      "timestamp": "2026-03-15T10:23:00Z"
    },
    {
      "run_id": "eval-another-case-with_skill",
      "feedback": "",
      "timestamp": "2026-03-15T10:24:00Z"
    }
  ],
  "status": "complete"
}
```

- Empty `feedback` string means the user had no issues with that eval
- Focus skill improvements on evals with non-empty feedback