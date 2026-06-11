#!/usr/bin/env python3
"""Generate all 30 fixtures for p118 (Pascal's Triangle, n in [1, 30])."""
import os, json

def generate(n):
    rows = [[1]]
    for _ in range(n - 1):
        r = rows[-1]
        rows.append([a + b for a, b in zip([0] + r, r + [0])])
    return rows

out = os.path.join(os.path.dirname(__file__), '..', 'fixtures', 'p118')
os.makedirs(out, exist_ok=True)

for n in range(1, 31):
    with open(os.path.join(out, f'{n:02d}.in'),  'w') as f: f.write(f'{n}\n')
    with open(os.path.join(out, f'{n:02d}.out'), 'w') as f: f.write(json.dumps(generate(n)) + '\n')

print(f'Generated 30 fixtures in fixtures/p118/')
