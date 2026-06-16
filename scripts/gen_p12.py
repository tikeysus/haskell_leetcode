#!/usr/bin/env python3
"""Generate 3999 fixtures for p12 (Integer to Roman, num in [1,3999])."""
import os

TABLE = [
    (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
    (100,  'C'), (90,  'XC'), (50,  'L'), (40,  'XL'),
    (10,   'X'), (9,   'IX'), (5,   'V'), (4,   'IV'),
    (1,    'I'),
]

def int_to_roman(n):
    result = ''
    for v, s in TABLE:
        q, n = divmod(n, v)
        result += s * q
    return result

OUT = os.path.join(os.path.dirname(__file__), '..', 'fixtures', 'p12')
os.makedirs(OUT, exist_ok=True)

for num in range(1, 4000):
    with open(os.path.join(OUT, f'{num:04d}.in'),  'w') as f: f.write(f'{num}\n')
    with open(os.path.join(OUT, f'{num:04d}.out'), 'w') as f: f.write(f'{int_to_roman(num)}\n')

print('Generated 3999 fixtures in fixtures/p12/')
