#!/usr/bin/env python3
"""Generate 15 fixtures for p526 (Beautiful Arrangement, n in [1,15])."""
import os

def count_arrangement(n):
    count = [0]
    used = [False] * (n + 1)
    def bt(pos):
        if pos > n:
            count[0] += 1
            return
        for x in range(1, n + 1):
            if not used[x] and (pos % x == 0 or x % pos == 0):
                used[x] = True
                bt(pos + 1)
                used[x] = False
    bt(1)
    return count[0]

OUT = os.path.join(os.path.dirname(__file__), '..', 'fixtures', 'p526')
os.makedirs(OUT, exist_ok=True)

for n in range(1, 16):
    with open(os.path.join(OUT, f'{n:02d}.in'),  'w') as f: f.write(f'{n}\n')
    with open(os.path.join(OUT, f'{n:02d}.out'), 'w') as f: f.write(f'{count_arrangement(n)}\n')

print('Generated 15 fixtures in fixtures/p526/')
