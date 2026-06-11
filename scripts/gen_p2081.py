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

def decimal_palindromes():
    """Yield all positive decimal palindromes in ascending order."""
    # length 1: 1-9
    for d in range(1, 10):
        yield d
    # even and odd lengths >= 2
    length = 2
    while True:
        half = (length + 1) // 2
        start = 10 ** (half - 1)
        end   = 10 ** half
        for prefix in range(start, end):
            s = str(prefix)
            if length % 2 == 0:
                pal = s + s[::-1]
            else:
                pal = s + s[-2::-1]
            yield int(pal)
        length += 1

def k_mirror(k, n):
    total = 0
    count = 0
    for num in decimal_palindromes():
        if is_palindrome(to_base(num, k)):
            total += num
            count += 1
            if count == n:
                return total
    return total  # unreachable

OUT = os.path.join(os.path.dirname(__file__), '..', 'fixtures', 'p2081')
os.makedirs(OUT, exist_ok=True)

# clear any partial fixtures
import glob
for f in glob.glob(os.path.join(OUT, '*')):
    os.remove(f)

idx = 0
for k in range(2, 10):
    for n in range(1, 31):
        with open(os.path.join(OUT, f'{idx:03d}.in'),  'w') as f: f.write(f'{k}\n{n}\n')
        with open(os.path.join(OUT, f'{idx:03d}.out'), 'w') as f: f.write(f'{k_mirror(k, n)}\n')
        idx += 1

print(f'Generated {idx} fixtures in fixtures/p2081/')
