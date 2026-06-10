#!/usr/bin/env python3
"""Generate all 31 fixtures for p509 (Fibonacci Number, n in [0, 30])."""
import os

fibs = [0, 1]
while len(fibs) < 31:
    fibs.append(fibs[-1] + fibs[-2])

out = os.path.join(os.path.dirname(__file__), '..', 'fixtures', 'p509')
os.makedirs(out, exist_ok=True)

for n, f in enumerate(fibs):
    with open(os.path.join(out, f'{n:02d}.in'), 'w') as fp:
        fp.write(f'{n}\n')
    with open(os.path.join(out, f'{n:02d}.out'), 'w') as fp:
        fp.write(f'{f}\n')

print(f'Generated {len(fibs)} fixtures in fixtures/p509/')
