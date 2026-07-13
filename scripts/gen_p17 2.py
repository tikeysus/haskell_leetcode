#!/usr/bin/env python3
"""Generate 4680 fixtures for p17 (Letter Combinations of a Phone Number)."""
import os, json

DIGITS = {
    '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
    '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz',
}

def letter_combinations(digits):
    result = ['']
    for d in digits:
        result = [prev + c for prev in result for c in DIGITS[d]]
    return sorted(result)

OUT = os.path.join(os.path.dirname(__file__), '..', 'fixtures', 'p17')
os.makedirs(OUT, exist_ok=True)

from itertools import product

idx = 0
for length in range(1, 5):
    for combo in product('23456789', repeat=length):
        digits = ''.join(combo)
        combos = letter_combinations(digits)
        with open(os.path.join(OUT, f'{idx:04d}.in'),  'w') as f: f.write(digits + '\n')
        with open(os.path.join(OUT, f'{idx:04d}.out'), 'w') as f: f.write(json.dumps(combos) + '\n')
        idx += 1

print(f'Generated {idx} fixtures in fixtures/p17/')
