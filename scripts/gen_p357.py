#!/usr/bin/env python3
"""Generate 9 fixtures for p357 (Count Numbers with Unique Digits, n in [0,8])."""
import os

def count_numbers_with_unique_digits(n):
    if n == 0:
        return 1
    count = 10
    unique = 9
    for k in range(2, n + 1):
        unique *= (11 - k)
        count += unique
    return count

OUT = os.path.join(os.path.dirname(__file__), '..', 'fixtures', 'p357')
os.makedirs(OUT, exist_ok=True)

for n in range(9):
    with open(os.path.join(OUT, f'{n:02d}.in'),  'w') as f: f.write(f'{n}\n')
    with open(os.path.join(OUT, f'{n:02d}.out'), 'w') as f: f.write(f'{count_numbers_with_unique_digits(n)}\n')

print('Generated 9 fixtures in fixtures/p357/')
