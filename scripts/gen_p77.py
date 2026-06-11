#!/usr/bin/env python3
"""Generate all 210 fixtures for p77 (Combinations, 1<=k<=n<=20)."""
import os, json

def combine(n, k):
    result = []
    def go(start, remaining, curr):
        if remaining == 0:
            result.append(list(curr))
            return
        for x in range(start, n + 1):
            curr.append(x)
            go(x + 1, remaining - 1, curr)
            curr.pop()
    go(1, k, [])
    return result

out = os.path.join(os.path.dirname(__file__), '..', 'fixtures', 'p77')
os.makedirs(out, exist_ok=True)

idx = 0
for n in range(1, 21):
    for k in range(1, n + 1):
        combos = combine(n, k)
        with open(os.path.join(out, f'{idx:03d}.in'),  'w') as f: f.write(f'{n}\n{k}\n')
        with open(os.path.join(out, f'{idx:03d}.out'), 'w') as f: f.write(json.dumps(combos) + '\n')
        idx += 1

print(f'Generated {idx} fixtures in fixtures/p77/')
