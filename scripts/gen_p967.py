#!/usr/bin/env python3
"""Generate all 80 fixtures for p967 (Numbers With Same Consecutive Differences, n in [2,9], k in [0,9])."""
import os, json

def nums_same_consec_diff(n, k):
    if n == 1:
        return list(range(10))
    result = []
    def go(remaining, last, acc):
        if remaining == 0:
            result.append(acc)
            return
        hi = last + k
        lo = last - k
        if hi <= 9:
            go(remaining - 1, hi, acc * 10 + hi)
        if k != 0 and lo >= 0:
            go(remaining - 1, lo, acc * 10 + lo)
    for d in range(1, 10):
        go(n - 1, d, d)
    return result

out = os.path.join(os.path.dirname(__file__), '..', 'fixtures', 'p967')
os.makedirs(out, exist_ok=True)

idx = 0
for n in range(2, 10):
    for k in range(0, 10):
        nums = nums_same_consec_diff(n, k)
        with open(os.path.join(out, f'{idx:03d}.in'),  'w') as f: f.write(f'{n}\n{k}\n')
        with open(os.path.join(out, f'{idx:03d}.out'), 'w') as f: f.write(json.dumps(nums) + '\n')
        idx += 1

print(f'Generated {idx} fixtures in fixtures/p967/')
