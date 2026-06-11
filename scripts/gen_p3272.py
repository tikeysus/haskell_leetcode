#!/usr/bin/env python3
"""Generate all 90 fixtures for p3272 (Find the Count of Good Integers, n in [1,10], k in [1,9])."""
import os
from math import factorial
from collections import Counter

def make_palindrome(n, prefix):
    s = str(prefix)
    if n % 2 == 1:
        return s + s[:-1][::-1]
    else:
        return s + s[::-1]

def count_perms(digits):
    n = len(digits)
    cnt = Counter(digits)
    total = factorial(n)
    for c in cnt.values():
        total //= factorial(c)
    if '0' in cnt:
        cnt2 = Counter(cnt)
        cnt2['0'] -= 1
        lead = factorial(n - 1)
        for c in cnt2.values():
            lead //= factorial(c)
        return total - lead
    return total

def count_good_integers(n, k):
    half = (n + 1) // 2
    lo = 10 ** (half - 1) if half > 1 else 1
    hi = 10 ** half - 1
    seen = set()
    for prefix in range(lo, hi + 1):
        pal = make_palindrome(n, prefix)
        if int(pal) % k == 0:
            seen.add(tuple(sorted(pal)))
    return sum(count_perms(d) for d in seen)

out = os.path.join(os.path.dirname(__file__), '..', 'fixtures', 'p3272')
os.makedirs(out, exist_ok=True)

idx = 0
for n in range(1, 11):
    for k in range(1, 10):
        result = count_good_integers(n, k)
        with open(os.path.join(out, f'{idx:03d}.in'),  'w') as f: f.write(f'{n}\n{k}\n')
        with open(os.path.join(out, f'{idx:03d}.out'), 'w') as f: f.write(f'{result}\n')
        idx += 1

print(f'Generated {idx} fixtures in fixtures/p3272/')
