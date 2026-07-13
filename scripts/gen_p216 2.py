#!/usr/bin/env python3
"""Generate 480 fixtures for p216 (Combination Sum III, 2<=k<=9, 1<=n<=60)."""
import os, json

def combination_sum3(k, n):
    result = []
    def go(start, remaining, curr):
        if remaining == 0 and len(curr) == k:
            result.append(list(curr))
            return
        if len(curr) == k or start > 9:
            return
        for x in range(start, 10):
            if x <= remaining:
                curr.append(x)
                go(x + 1, remaining - x, curr)
                curr.pop()
    go(1, n, [])
    return result

OUT = os.path.join(os.path.dirname(__file__), '..', 'fixtures', 'p216')
os.makedirs(OUT, exist_ok=True)

idx = 0
for k in range(2, 10):
    for n in range(1, 61):
        combos = combination_sum3(k, n)
        with open(os.path.join(OUT, f'{idx:03d}.in'),  'w') as f: f.write(f'{k}\n{n}\n')
        with open(os.path.join(OUT, f'{idx:03d}.out'), 'w') as f: f.write(json.dumps(combos) + '\n')
        idx += 1

print(f'Generated {idx} fixtures in fixtures/p216/')
