#!/usr/bin/env python3
"""Generate all 8 fixtures for p95 (Unique Binary Search Trees II)."""
import os, json
from collections import deque

def oracle(lo, hi):
    if lo > hi:
        return [None]
    result = []
    for i in range(lo, hi + 1):
        for left in oracle(lo, i - 1):
            for right in oracle(i + 1, hi):
                result.append((i, left, right))
    return result

def serialize(tree):
    if tree is None:
        return []
    out = []
    q = deque([tree])
    while q:
        node = q.popleft()
        if node is None:
            out.append(None)
        else:
            val, left, right = node
            out.append(val)
            q.append(left)
            q.append(right)
    while out and out[-1] is None:
        out.pop()
    return out

OUT = os.path.join(os.path.dirname(__file__), '..', 'fixtures', 'p95')
os.makedirs(OUT, exist_ok=True)

for n in range(1, 9):
    trees = oracle(1, n)
    serialized = [serialize(t) for t in trees]
    idx = n - 1
    with open(os.path.join(OUT, f'{idx:02d}.in'),  'w') as f: f.write(f'{n}\n')
    with open(os.path.join(OUT, f'{idx:02d}.out'), 'w') as f:
        f.write(json.dumps(serialized, separators=(',', ':')) + '\n')

print(f'Generated 8 fixtures in fixtures/p95/')
