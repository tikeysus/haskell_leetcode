#!/usr/bin/env python3
"""Generate 1690 fixtures for p264 (Nth Ugly Number, n in [1,1690])."""
import os

def generate_ugly(count):
    ugly = [1] * count
    i2 = i3 = i5 = 0
    for i in range(1, count):
        n2, n3, n5 = ugly[i2] * 2, ugly[i3] * 3, ugly[i5] * 5
        ugly[i] = min(n2, n3, n5)
        if ugly[i] == n2: i2 += 1
        if ugly[i] == n3: i3 += 1
        if ugly[i] == n5: i5 += 1
    return ugly

OUT = os.path.join(os.path.dirname(__file__), '..', 'fixtures', 'p264')
os.makedirs(OUT, exist_ok=True)

ugly = generate_ugly(1690)
for n in range(1, 1691):
    with open(os.path.join(OUT, f'{n:04d}.in'),  'w') as f: f.write(f'{n}\n')
    with open(os.path.join(OUT, f'{n:04d}.out'), 'w') as f: f.write(f'{ugly[n - 1]}\n')

print('Generated 1690 fixtures in fixtures/p264/')
