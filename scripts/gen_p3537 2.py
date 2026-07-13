#!/usr/bin/env python3
"""Generate 8 fixtures for p3537 (Fill a Special Grid, n in [0,7])."""
import os, json

def special_grid(n):
    size = 1 << n
    grid = [[0] * size for _ in range(size)]
    fill(grid, 0, 0, size, 0)
    return grid

def fill(grid, row, col, size, start):
    if size == 1:
        grid[row][col] = start
        return
    half = size // 2
    quarter = half * half
    # top-left gets largest values, top-right smallest, bottom follows
    # Constraint: top-right < top-left, bottom-right < bottom-left,
    # bottom-left < top-left, bottom-right < top-right
    # Canonical assignment: top-right=[start..], bottom-right=[start+q..],
    # bottom-left=[start+2q..], top-left=[start+3q..]
    fill(grid, row,        col + half, half, start)
    fill(grid, row + half, col + half, half, start + quarter)
    fill(grid, row + half, col,        half, start + 2 * quarter)
    fill(grid, row,        col,        half, start + 3 * quarter)

OUT = os.path.join(os.path.dirname(__file__), '..', 'fixtures', 'p3537')
os.makedirs(OUT, exist_ok=True)

for n in range(8):
    grid = special_grid(n)
    with open(os.path.join(OUT, f'{n:02d}.in'),  'w') as f: f.write(f'{n}\n')
    with open(os.path.join(OUT, f'{n:02d}.out'), 'w') as f: f.write(json.dumps(grid) + '\n')

print('Generated 8 fixtures in fixtures/p3537/')
