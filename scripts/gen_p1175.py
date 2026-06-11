#!/usr/bin/env python3
"""Generate all 100 fixtures for p1175 (Prime Arrangements, n in [1, 100])."""
import os
from math import factorial

MOD = 10**9 + 7

def is_prime(x):
    if x < 2: return False
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0: return False
    return True

out = os.path.join(os.path.dirname(__file__), '..', 'fixtures', 'p1175')
os.makedirs(out, exist_ok=True)

for n in range(1, 101):
    p = sum(1 for x in range(2, n + 1) if is_prime(x))
    result = (factorial(p) * factorial(n - p)) % MOD
    with open(os.path.join(out, f'{n:03d}.in'),  'w') as f: f.write(f'{n}\n')
    with open(os.path.join(out, f'{n:03d}.out'), 'w') as f: f.write(f'{result}\n')

print(f'Generated 100 fixtures in fixtures/p1175/')
