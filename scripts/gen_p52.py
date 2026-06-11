#!/usr/bin/env python3
"""Generate all 9 fixtures for p52 (N-Queens II, n in [1, 9])."""
import os

def total_n_queens(n):
    count = [0]
    def place(row, cols, diag1, diag2):
        if row == n:
            count[0] += 1
            return
        for col in range(n):
            if col in cols or (row - col) in diag1 or (row + col) in diag2:
                continue
            place(row+1, cols | {col}, diag1 | {row-col}, diag2 | {row+col})
    place(0, set(), set(), set())
    return count[0]

out = os.path.join(os.path.dirname(__file__), '..', 'fixtures', 'p52')
os.makedirs(out, exist_ok=True)

for n in range(1, 10):
    with open(os.path.join(out, f'{n:02d}.in'),  'w') as f: f.write(f'{n}\n')
    with open(os.path.join(out, f'{n:02d}.out'), 'w') as f: f.write(f'{total_n_queens(n)}\n')

print(f'Generated 9 fixtures in fixtures/p52/')
