#!/usr/bin/env python3
"""Generate fixtures for p894 (All Possible Full Binary Trees, odd n in [1,19])."""
import os, json
from collections import deque

_MISSING = object()  # absent child slot (distinct from a leaf node)

def oracle(n):
    """Return list of trees: None = leaf, (left, right) = internal node."""
    if n == 1:
        return [None]
    if n % 2 == 0:
        return []
    result = []
    for i in range(1, n - 1, 2):
        for left in oracle(i):
            for right in oracle(n - 1 - i):
                result.append((left, right))
    return result

def to_leetcode(tree):
    """BFS serialisation matching LeetCode format; all node values are 0."""
    out = []
    q = deque([tree])
    while q:
        node = q.popleft()
        if node is _MISSING:
            out.append(None)
        elif node is None:          # leaf
            out.append(0)
            q.append(_MISSING)
            q.append(_MISSING)
        else:                       # internal
            left, right = node
            out.append(0)
            q.append(left)
            q.append(right)
    while out and out[-1] is None:
        out.pop()
    return out

def dumps(obj):
    return json.dumps(obj, separators=(',', ':'))

OUT = os.path.join(os.path.dirname(__file__), '..', 'fixtures', 'p894')
os.makedirs(OUT, exist_ok=True)

idx = 0
for n in range(1, 20, 2):
    trees = [to_leetcode(t) for t in oracle(n)]
    with open(os.path.join(OUT, f'{idx:02d}.in'),  'w') as f: f.write(f'{n}\n')
    with open(os.path.join(OUT, f'{idx:02d}.out'), 'w') as f: f.write(dumps(trees) + '\n')
    idx += 1

print(f'Generated {idx} fixtures in fixtures/p894/')
