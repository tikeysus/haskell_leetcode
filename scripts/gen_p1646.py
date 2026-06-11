#!/usr/bin/env python3
"""Generate all 101 fixtures for p1646 (Get Maximum in Generated Array, n in [0, 100])."""
import os

def get_max(n):
    if n == 0: return 0
    nums = [0, 1]
    for i in range(2, n + 1):
        if i % 2 == 0:
            nums.append(nums[i // 2])
        else:
            nums.append(nums[i // 2] + nums[i // 2 + 1])
    return max(nums)

out = os.path.join(os.path.dirname(__file__), '..', 'fixtures', 'p1646')
os.makedirs(out, exist_ok=True)

for n in range(0, 101):
    with open(os.path.join(out, f'{n:03d}.in'),  'w') as f: f.write(f'{n}\n')
    with open(os.path.join(out, f'{n:03d}.out'), 'w') as f: f.write(f'{get_max(n)}\n')

print(f'Generated 101 fixtures in fixtures/p1646/')
