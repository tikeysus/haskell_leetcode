#!/usr/bin/env python3
"""Generate 15 fixtures for p526 (Beautiful Arrangement, n in [1,15])."""
import os
from functools import lru_cache

def count_arrangement(n):
    @lru_cache(maxsize=None)
    def go(pos, used):
        if pos > n:
            return 1
        total = 0
        for k in range(1, n+1):
            if not (used >> k & 1) and (k % pos == 0 or pos % k == 0):
                total += go(pos+1, used | (1 << k))
        return total
    return go(1, 0)

OUT = os.path.join(os.path.dirname(__file__), '..', 'fixtures', 'p526')
os.makedirs(OUT, exist_ok=True)

for n in range(1, 16):
    idx = f'{n-1:02d}'
    with open(os.path.join(OUT, f'{idx}.in'),  'w') as f: f.write(f'{n}\n')
    with open(os.path.join(OUT, f'{idx}.out'), 'w') as f: f.write(str(count_arrangement(n)) + '\n')

print('Generated 15 fixtures in fixtures/p526/')
