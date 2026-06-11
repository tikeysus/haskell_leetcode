#!/usr/bin/env python3
"""Generate all 50 fixtures for p1641 (Count Sorted Vowel Strings, n in [1, 50])."""
import os
from math import comb

out = os.path.join(os.path.dirname(__file__), '..', 'fixtures', 'p1641')
os.makedirs(out, exist_ok=True)

for n in range(1, 51):
    result = comb(n + 4, 4)
    with open(os.path.join(out, f'{n:02d}.in'),  'w') as f: f.write(f'{n}\n')
    with open(os.path.join(out, f'{n:02d}.out'), 'w') as f: f.write(f'{result}\n')

print(f'Generated 50 fixtures in fixtures/p1641/')
