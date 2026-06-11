#!/usr/bin/env python3
"""Generate all 100 fixtures for p1447 (Simplified Fractions, n in [1, 100])."""
import os, json
from math import gcd

out = os.path.join(os.path.dirname(__file__), '..', 'fixtures', 'p1447')
os.makedirs(out, exist_ok=True)

for n in range(1, 101):
    fracs = [f'{a}/{b}' for b in range(2, n + 1) for a in range(1, b) if gcd(a, b) == 1]
    with open(os.path.join(out, f'{n:03d}.in'),  'w') as f: f.write(f'{n}\n')
    with open(os.path.join(out, f'{n:03d}.out'), 'w') as f: f.write(json.dumps(fracs) + '\n')

print(f'Generated 100 fixtures in fixtures/p1447/')
