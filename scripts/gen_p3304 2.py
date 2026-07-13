#!/usr/bin/env python3
"""Generate all 500 fixtures for p3304 (Find the K-th Character in String Game I, k in [1,500])."""
import os

def kth_character(k):
    word = [0]
    while len(word) < k:
        word += [(c + 1) % 26 for c in word]
    return chr(ord('a') + word[k - 1])

OUT = os.path.join(os.path.dirname(__file__), '..', 'fixtures', 'p3304')
os.makedirs(OUT, exist_ok=True)

for k in range(1, 501):
    with open(os.path.join(OUT, f'{k:03d}.in'),  'w') as f: f.write(f'{k}\n')
    with open(os.path.join(OUT, f'{k:03d}.out'), 'w') as f: f.write(kth_character(k) + '\n')

print('Generated 500 fixtures in fixtures/p3304/')
