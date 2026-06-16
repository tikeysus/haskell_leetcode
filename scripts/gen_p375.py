#!/usr/bin/env python3
"""Generate 200 fixtures for p375 (Guess Number Higher or Lower II, n in [1,200])."""
import os
from functools import lru_cache

@lru_cache(maxsize=None)
def get_money_amount(i, j):
    if i >= j:
        return 0
    return min(k + max(get_money_amount(i, k-1), get_money_amount(k+1, j))
               for k in range(i, j+1))

OUT = os.path.join(os.path.dirname(__file__), '..', 'fixtures', 'p375')
os.makedirs(OUT, exist_ok=True)

for n in range(1, 201):
    idx = f'{n-1:03d}'
    with open(os.path.join(OUT, f'{idx}.in'),  'w') as f: f.write(f'{n}\n')
    with open(os.path.join(OUT, f'{idx}.out'), 'w') as f: f.write(str(get_money_amount(1, n)) + '\n')

print('Generated 200 fixtures in fixtures/p375/')
