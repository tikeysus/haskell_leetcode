#!/usr/bin/env python3
"""Generate fixtures for p4 (Median of Two Sorted Arrays)."""
import ast, json, os, re

DATA = os.path.join(os.path.expanduser("~"), "Documents", "projects",
                    "leetcode-testcase-extractor", "data",
                    "4. Median of Two Sorted Arrays")
OUT  = os.path.join(os.path.dirname(__file__), "..", "fixtures", "p4")
os.makedirs(OUT, exist_ok=True)

def parse_cases(path):
    cases = []
    for line in open(path):
        m = re.match(r'\s+if (.+): return (.+)', line.rstrip())
        if not m:
            continue
        try:
            ret  = ast.literal_eval(m.group(2).strip())
            tree = ast.parse(m.group(1), mode='eval')
            args = {}
            def collect(node):
                if isinstance(node, ast.BoolOp):
                    for v in node.values: collect(v)
                elif isinstance(node, ast.Compare):
                    args[node.left.id] = ast.literal_eval(node.comparators[0])
            collect(tree.body)
            cases.append((args, ret))
        except Exception:
            pass
    return cases

cases = parse_cases(DATA)
for i, (args, ret) in enumerate(cases):
    with open(os.path.join(OUT, f"{i:03d}.in"),  "w") as f:
        f.write(json.dumps(args["nums1"]) + "\n" + json.dumps(args["nums2"]) + "\n")
    with open(os.path.join(OUT, f"{i:03d}.out"), "w") as f:
        f.write(f"{ret:.5f}\n")

print(f"Generated {len(cases)} fixtures in fixtures/p4/")
