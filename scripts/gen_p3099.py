#!/usr/bin/env python3
"""Generate all 100 fixtures for p3099 (Harshad Number, x in [1, 100])."""
import os

out = os.path.join(os.path.dirname(__file__), '..', 'fixtures', 'p3099')
os.makedirs(out, exist_ok=True)

for x in range(1, 101):
    s = sum(int(c) for c in str(x))
    result = x if x % s == 0 else -1
    with open(os.path.join(out, f'{x:03d}.in'),  'w') as f: f.write(f'{x}\n')
    with open(os.path.join(out, f'{x:03d}.out'), 'w') as f: f.write(f'{result}\n')

print(f'Generated 100 fixtures in fixtures/p3099/')
