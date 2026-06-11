#!/usr/bin/env python3
"""Generate all 18 fixtures for p3211 (Generate Binary Strings Without Adjacent Zeros, n in [1, 18])."""
import os, json

def valid_strings(n):
    result = []
    def go(k, prev, curr):
        if k == 0:
            result.append(curr)
            return
        go(k-1, '1', curr + '1')
        if prev == '1':
            go(k-1, '0', curr + '0')
    go(n, '1', '')
    return result

out = os.path.join(os.path.dirname(__file__), '..', 'fixtures', 'p3211')
os.makedirs(out, exist_ok=True)

for n in range(1, 19):
    strings = valid_strings(n)
    with open(os.path.join(out, f'{n:02d}.in'),  'w') as f: f.write(f'{n}\n')
    with open(os.path.join(out, f'{n:02d}.out'), 'w') as f: f.write(json.dumps(strings) + '\n')

print(f'Generated 18 fixtures in fixtures/p3211/')
