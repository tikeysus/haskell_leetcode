#!/usr/bin/env python3
"""Generate fixtures for p3 (Longest Substring Without Repeating Characters)."""
import ast, os, re

DATA = os.path.join(os.path.expanduser("~"), "Documents", "projects",
                    "leetcode-testcase-extractor", "data",
                    "3. Longest Substring Without Repeating Characters")
OUT  = os.path.join(os.path.dirname(__file__), "..", "fixtures", "p3")
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
        f.write(args["s"] + "\n")
    with open(os.path.join(OUT, f"{i:03d}.out"), "w") as f:
        f.write(str(ret) + "\n")

print(f"Generated {len(cases)} fixtures in fixtures/p3/")
