#!/usr/bin/env python3
"""Generate 10001 fixtures for p172 (Factorial Trailing Zeroes, n in [0,10000])."""
import os

def trailing_zeroes(n):
    count = 0
    while n >= 5:
        n //= 5
        count += n
    return count

OUT = os.path.join(os.path.dirname(__file__), '..', 'fixtures', 'p172')
os.makedirs(OUT, exist_ok=True)

for n in range(10001):
    with open(os.path.join(OUT, f'{n:05d}.in'),  'w') as f: f.write(f'{n}\n')
    with open(os.path.join(OUT, f'{n:05d}.out'), 'w') as f: f.write(f'{trailing_zeroes(n)}\n')

print('Generated 10001 fixtures in fixtures/p172/')
