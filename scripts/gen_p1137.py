#!/usr/bin/env python3
"""Generate all 38 fixtures for p1137 (N-th Tribonacci Number, n in [0, 37])."""
import os

tribs = [0, 1, 1]
while len(tribs) < 38:
    tribs.append(tribs[-1] + tribs[-2] + tribs[-3])

out = os.path.join(os.path.dirname(__file__), '..', 'fixtures', 'p1137')
os.makedirs(out, exist_ok=True)

for n, t in enumerate(tribs):
    with open(os.path.join(out, f'{n:02d}.in'),  'w') as f: f.write(f'{n}\n')
    with open(os.path.join(out, f'{n:02d}.out'), 'w') as f: f.write(f'{t}\n')

print(f'Generated {len(tribs)} fixtures in fixtures/p1137/')
