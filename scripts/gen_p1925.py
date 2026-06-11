#!/usr/bin/env python3
"""Generate all 250 fixtures for p1925 (Count Square Sum Triples, n in [1,250])."""
import os

def count_triples(n):
    count = 0
    squares = set(i*i for i in range(1, n+1))
    for a in range(1, n+1):
        for b in range(1, n+1):
            if a*a + b*b in squares:
                count += 1
    return count

OUT = os.path.join(os.path.dirname(__file__), '..', 'fixtures', 'p1925')
os.makedirs(OUT, exist_ok=True)

for n in range(1, 251):
    with open(os.path.join(OUT, f'{n:03d}.in'),  'w') as f: f.write(f'{n}\n')
    with open(os.path.join(OUT, f'{n:03d}.out'), 'w') as f: f.write(f'{count_triples(n)}\n')

print('Generated 250 fixtures in fixtures/p1925/')
