#!/usr/bin/env python3
"""Generate 10000 fixtures for p279 (Perfect Squares, n in [1,10000])."""
import os
import math

def num_squares(n):
    if int(math.isqrt(n)) ** 2 == n:
        return 1
    # Check if n is of the form 4^a(8b+7)
    x = n
    while x % 4 == 0:
        x //= 4
    if x % 8 == 7:
        return 4
    # Check if n = a^2 + b^2
    for a in range(1, int(math.isqrt(n)) + 1):
        b2 = n - a * a
        if int(math.isqrt(b2)) ** 2 == b2:
            return 2
    return 3

OUT = os.path.join(os.path.dirname(__file__), '..', 'fixtures', 'p279')
os.makedirs(OUT, exist_ok=True)

for n in range(1, 10001):
    with open(os.path.join(OUT, f'{n:05d}.in'),  'w') as f: f.write(f'{n}\n')
    with open(os.path.join(OUT, f'{n:05d}.out'), 'w') as f: f.write(f'{num_squares(n)}\n')

print('Generated 10000 fixtures in fixtures/p279/')
