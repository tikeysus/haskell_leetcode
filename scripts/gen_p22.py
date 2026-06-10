#!/usr/bin/env python3
"""Generate all 8 fixtures for p22 (Generate Parentheses, n in [1, 8])."""
import os, json

def gen_parens(n):
    result = []
    def go(open, close, curr):
        if len(curr) == 2 * n:
            result.append(curr)
            return
        if open < n:     go(open + 1, close,     curr + '(')
        if close < open: go(open,     close + 1, curr + ')')
    go(0, 0, '')
    return sorted(result)

out = os.path.join(os.path.dirname(__file__), '..', 'fixtures', 'p22')
os.makedirs(out, exist_ok=True)

for n in range(1, 9):
    combos = gen_parens(n)
    with open(os.path.join(out, f'{n:02d}.in'),  'w') as f: f.write(f'{n}\n')
    with open(os.path.join(out, f'{n:02d}.out'), 'w') as f: f.write(json.dumps(combos) + '\n')

print(f'Generated 8 fixtures in fixtures/p22/')
