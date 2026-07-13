#!/usr/bin/env python3
"""Generate all 34 fixtures for p119 (Pascal's Triangle II, rowIndex in [0,33])."""
import os, json

def get_row(n):
    row = [1]
    for _ in range(n):
        row = [a + b for a, b in zip([0] + row, row + [0])]
    return row

OUT = os.path.join(os.path.dirname(__file__), '..', 'fixtures', 'p119')
os.makedirs(OUT, exist_ok=True)

for i in range(34):
    with open(os.path.join(OUT, f'{i:02d}.in'),  'w') as f: f.write(f'{i}\n')
    with open(os.path.join(OUT, f'{i:02d}.out'), 'w') as f: f.write(json.dumps(get_row(i)) + '\n')

print('Generated 34 fixtures in fixtures/p119/')
