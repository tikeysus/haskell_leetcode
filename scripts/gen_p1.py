#!/usr/bin/env python3
"""Generate fixtures for p1 (Two Sum) from extracted test cases."""
import json, os

DATA = os.path.join(os.path.expanduser("~"), "Documents", "projects",
                    "leetcode-testcase-extractor", "data", "1. Two Sum")
OUT  = os.path.join(os.path.dirname(__file__), "..", "fixtures", "p1")
os.makedirs(OUT, exist_ok=True)

def parse_cases(path):
    cases = []
    for line in open(path):
        line = line.strip()
        if not line:
            continue
        try:
            obj = json.loads(line)
            cases.append((obj["args"], obj["ret"]))
        except Exception:
            pass
    return cases

cases = parse_cases(DATA)
for i, (args, ret) in enumerate(cases):
    with open(os.path.join(OUT, f"{i:02d}.in"),  "w") as f:
        f.write(json.dumps(args["nums"]) + "\n" + str(args["target"]) + "\n")
    with open(os.path.join(OUT, f"{i:02d}.out"), "w") as f:
        f.write(json.dumps(ret) + "\n")

print(f"Generated {len(cases)} fixtures in fixtures/p1/")
