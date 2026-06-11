#!/usr/bin/env python3
"""Generate all 45 fixtures for p70 (Climbing Stairs, n in [1, 45])."""
import os

fibs = [0, 1]
while len(fibs) < 47:
    fibs.append(fibs[-1] + fibs[-2])

out = os.path.join(os.path.dirname(__file__), '..', 'fixtures', 'p70')
os.makedirs(out, exist_ok=True)

for n in range(1, 46):
    with open(os.path.join(out, f'{n:02d}.in'),  'w') as f: f.write(f'{n}\n')
    with open(os.path.join(out, f'{n:02d}.out'), 'w') as f: f.write(f'{fibs[n+1]}\n')

print(f'Generated 45 fixtures in fixtures/p70/')
