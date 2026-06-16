#!/usr/bin/env python3
"""Generate 8 fixtures for p479 (Largest Palindrome Product, n in [1,8])."""
import os

def largest_palindrome(n):
    if n == 1:
        return 9
    upper = 10 ** n - 1
    lower = 10 ** (n - 1)
    for a in range(upper, lower - 1, -1):
        s = str(a)
        pal = int(s + s[::-1])
        b = upper
        while b * b >= pal:
            if pal % b == 0 and pal // b >= lower:
                return pal % 1337
            b -= 1
    return 9

OUT = os.path.join(os.path.dirname(__file__), '..', 'fixtures', 'p479')
os.makedirs(OUT, exist_ok=True)

for n in range(1, 9):
    with open(os.path.join(OUT, f'{n:02d}.in'),  'w') as f: f.write(f'{n}\n')
    with open(os.path.join(OUT, f'{n:02d}.out'), 'w') as f: f.write(f'{largest_palindrome(n)}\n')

print('Generated 8 fixtures in fixtures/p479/')
