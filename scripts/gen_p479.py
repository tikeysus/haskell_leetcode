#!/usr/bin/env python3
"""Generate 8 fixtures for p479 (Largest Palindrome Product, n in [1,8])."""
import os, math

def largest_palindrome(n):
    if n == 1:
        return 9
    hi = 10**n - 1
    lo = 10**(n-1)
    for t in range(hi, lo-1, -1):
        s = str(t)
        p = int(s + s[::-1])
        if p > hi * hi:
            continue
        a = min(hi, p // lo)
        isqrt_p = math.isqrt(p)
        while a >= isqrt_p:
            if p % a == 0 and lo <= p // a <= hi:
                return p % 1337
            a -= 1
    return -1

OUT = os.path.join(os.path.dirname(__file__), '..', 'fixtures', 'p479')
os.makedirs(OUT, exist_ok=True)

for n in range(1, 9):
    idx = f'{n-1:02d}'
    with open(os.path.join(OUT, f'{idx}.in'),  'w') as f: f.write(f'{n}\n')
    with open(os.path.join(OUT, f'{idx}.out'), 'w') as f: f.write(str(largest_palindrome(n)) + '\n')

print('Generated 8 fixtures in fixtures/p479/')
