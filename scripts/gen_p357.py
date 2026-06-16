#!/usr/bin/env python3
"""Generate 9 fixtures for p357 (Count Numbers with Unique Digits, n in [0,8])."""
import os

def count_unique_digits(n):
    if n == 0:
        return 1
    result = 10
    choices = 9
    available = 9
    for _ in range(n - 1):
        choices *= available
        result += choices
        available -= 1
    return result

OUT = os.path.join(os.path.dirname(__file__), '..', 'fixtures', 'p357')
os.makedirs(OUT, exist_ok=True)

for n in range(9):
    with open(os.path.join(OUT, f'{n:02d}.in'),  'w') as f: f.write(f'{n}\n')
    with open(os.path.join(OUT, f'{n:02d}.out'), 'w') as f: f.write(str(count_unique_digits(n)) + '\n')

print('Generated 9 fixtures in fixtures/p357/')
