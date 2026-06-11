#!/usr/bin/env python3
"""Generate all 16 fixtures for p89 (Gray Code, n in [1, 16])."""
import os, json

def gray_code(n):
    return [i ^ (i >> 1) for i in range(2**n)]

out = os.path.join(os.path.dirname(__file__), '..', 'fixtures', 'p89')
os.makedirs(out, exist_ok=True)

for n in range(1, 17):
    with open(os.path.join(out, f'{n:02d}.in'),  'w') as f: f.write(f'{n}\n')
    with open(os.path.join(out, f'{n:02d}.out'), 'w') as f: f.write(json.dumps(gray_code(n)) + '\n')

print(f'Generated 16 fixtures in fixtures/p89/')
