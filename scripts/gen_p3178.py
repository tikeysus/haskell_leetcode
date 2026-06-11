#!/usr/bin/env python3
"""Generate all 2450 fixtures for p3178 (Find the Child Who Has the Ball After K Seconds)."""
import os

def number_of_child(n, k):
    period = 2 * (n - 1)
    pos = k % period
    return pos if pos <= n - 1 else period - pos

OUT = os.path.join(os.path.dirname(__file__), '..', 'fixtures', 'p3178')
os.makedirs(OUT, exist_ok=True)

idx = 0
for n in range(2, 51):
    for k in range(1, 51):
        with open(os.path.join(OUT, f'{idx:04d}.in'),  'w') as f: f.write(f'{n}\n{k}\n')
        with open(os.path.join(OUT, f'{idx:04d}.out'), 'w') as f: f.write(f'{number_of_child(n, k)}\n')
        idx += 1

print(f'Generated {idx} fixtures in fixtures/p3178/')
