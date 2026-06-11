#!/usr/bin/env python3
"""Generate all 11 fixtures for p401 (Binary Watch, turnedOn in [0, 10])."""
import os, json

def read_binary_watch(turned_on):
    result = []
    for h in range(12):
        for m in range(60):
            if bin(h).count('1') + bin(m).count('1') == turned_on:
                result.append(f'{h}:{m:02d}')
    return result

out = os.path.join(os.path.dirname(__file__), '..', 'fixtures', 'p401')
os.makedirs(out, exist_ok=True)

for n in range(11):
    times = read_binary_watch(n)
    with open(os.path.join(out, f'{n:02d}.in'),  'w') as f: f.write(f'{n}\n')
    with open(os.path.join(out, f'{n:02d}.out'), 'w') as f: f.write(json.dumps(times) + '\n')

print(f'Generated 11 fixtures in fixtures/p401/')
