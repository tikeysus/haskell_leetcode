#!/usr/bin/env python3
"""Generate all 9 fixtures for p51 (N-Queens, n in [1, 9])."""
import os, json

def solve_n_queens(n):
    solutions = []
    def place(row, cols, diag1, diag2, board):
        if row == n:
            solutions.append([''.join(r) for r in board])
            return
        for col in range(n):
            if col in cols or (row - col) in diag1 or (row + col) in diag2:
                continue
            row_str = ['.'] * n
            row_str[col] = 'Q'
            place(row+1, cols | {col}, diag1 | {row-col}, diag2 | {row+col},
                  board + [row_str])
    place(0, set(), set(), set(), [])
    return sorted(solutions)

out = os.path.join(os.path.dirname(__file__), '..', 'fixtures', 'p51')
os.makedirs(out, exist_ok=True)

for n in range(1, 10):
    sols = solve_n_queens(n)
    with open(os.path.join(out, f'{n:02d}.in'),  'w') as f: f.write(f'{n}\n')
    with open(os.path.join(out, f'{n:02d}.out'), 'w') as f: f.write(json.dumps(sols) + '\n')

print(f'Generated 9 fixtures in fixtures/p51/')
