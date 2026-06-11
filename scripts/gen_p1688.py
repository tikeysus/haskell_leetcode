#!/usr/bin/env python3
"""Generate all 200 fixtures for p1688 (Count of Matches in Tournament, n in [1, 200])."""
import os

out = os.path.join(os.path.dirname(__file__), '..', 'fixtures', 'p1688')
os.makedirs(out, exist_ok=True)

for n in range(1, 201):
    with open(os.path.join(out, f'{n:03d}.in'),  'w') as f: f.write(f'{n}\n')
    with open(os.path.join(out, f'{n:03d}.out'), 'w') as f: f.write(f'{n - 1}\n')

print(f'Generated 200 fixtures in fixtures/p1688/')
