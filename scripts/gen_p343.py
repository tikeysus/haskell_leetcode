#!/usr/bin/env python3
"""Generate 57 fixtures for p343 (Integer Break, n in [2,58])."""
import os

def integer_break(n):
    if n == 2: return 1
    if n == 3: return 2
    if n % 3 == 0: return 3 ** (n // 3)
    if n % 3 == 1: return 4 * 3 ** ((n - 4) // 3)
    return 2 * 3 ** ((n - 2) // 3)

OUT = os.path.join(os.path.dirname(__file__), '..', 'fixtures', 'p343')
os.makedirs(OUT, exist_ok=True)

for i, n in enumerate(range(2, 59)):
    with open(os.path.join(OUT, f'{i:02d}.in'),  'w') as f: f.write(f'{n}\n')
    with open(os.path.join(OUT, f'{i:02d}.out'), 'w') as f: f.write(f'{integer_break(n)}\n')

print('Generated 57 fixtures in fixtures/p343/')
