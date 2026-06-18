#!/usr/bin/env python3
"""Generate 10000 fixtures for p62 (Unique Paths, 1<=m,n<=100)."""
import os, math

OUT = os.path.join(os.path.dirname(__file__), '..', 'fixtures', 'p62')
os.makedirs(OUT, exist_ok=True)

idx = 0
for m in range(1, 101):
    for n in range(1, 101):
        result = math.comb(m + n - 2, m - 1)
        with open(os.path.join(OUT, f'{idx:05d}.in'),  'w') as f: f.write(f'{m}\n{n}\n')
        with open(os.path.join(OUT, f'{idx:05d}.out'), 'w') as f: f.write(f'{result}\n')
        idx += 1

print(f'Generated {idx} fixtures in fixtures/p62/')
