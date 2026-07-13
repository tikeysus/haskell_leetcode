#!/usr/bin/env python3
"""Generate 240 fixtures for p2081 (Sum of k-Mirror Numbers, 2<=k<=9, 1<=n<=30)."""
import os

def is_palindrome(s):
    return s == s[::-1]

def to_base(num, base):
    if num == 0:
        return '0'
    digits = []
    while num:
        digits.append(str(num % base))
        num //= base
    return ''.join(reversed(digits))

def k_mirror(k, n):
    total = 0
    count = 0
    num = 1
    while count < n:
        s = str(num)
        if is_palindrome(s) and is_palindrome(to_base(num, k)):
            total += num
            count += 1
        num += 1
    return total

OUT = os.path.join(os.path.dirname(__file__), '..', 'fixtures', 'p2081')
os.makedirs(OUT, exist_ok=True)

idx = 0
for k in range(2, 10):
    for n in range(1, 31):
        with open(os.path.join(OUT, f'{idx:03d}.in'),  'w') as f: f.write(f'{k}\n{n}\n')
        with open(os.path.join(OUT, f'{idx:03d}.out'), 'w') as f: f.write(f'{k_mirror(k, n)}\n')
        idx += 1

print(f'Generated {idx} fixtures in fixtures/p2081/')
