#!/usr/bin/env python3
"""Generate 1000 fixtures for p1415 (K-th Lexicographic Happy String of Length n)."""
import os

def get_happy_string(n, k):
    results = []
    def go(curr):
        if len(curr) == n:
            results.append(curr)
            return
        for c in 'abc':
            if not curr or curr[-1] != c:
                go(curr + c)
    go('')
    return results[k - 1] if k <= len(results) else ''

OUT = os.path.join(os.path.dirname(__file__), '..', 'fixtures', 'p1415')
os.makedirs(OUT, exist_ok=True)

idx = 0
for n in range(1, 11):
    for k in range(1, 101):
        result = get_happy_string(n, k)
        with open(os.path.join(OUT, f'{idx:04d}.in'),  'w') as f: f.write(f'{n}\n{k}\n')
        with open(os.path.join(OUT, f'{idx:04d}.out'), 'w') as f: f.write(result + '\n')
        idx += 1

print(f'Generated {idx} fixtures in fixtures/p1415/')
