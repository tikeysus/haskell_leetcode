#!/usr/bin/env python3
"""Generate all 19 fixtures for p96 (Unique Binary Search Trees, n in [1, 19])."""
import os

catalan = [1]
for k in range(1, 20):
    catalan.append(sum(catalan[i] * catalan[k-1-i] for i in range(k)))

out = os.path.join(os.path.dirname(__file__), '..', 'fixtures', 'p96')
os.makedirs(out, exist_ok=True)

for n in range(1, 20):
    with open(os.path.join(out, f'{n:02d}.in'),  'w') as f: f.write(f'{n}\n')
    with open(os.path.join(out, f'{n:02d}.out'), 'w') as f: f.write(f'{catalan[n]}\n')

print(f'Generated 19 fixtures in fixtures/p96/')
