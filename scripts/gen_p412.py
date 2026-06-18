#!/usr/bin/env python3
"""Generate 10000 fixtures for p412 (Fizz Buzz, n in [1,10000])."""
import os, json

def fizz_buzz(n):
    result = []
    for i in range(1, n + 1):
        if i % 15 == 0:
            result.append("FizzBuzz")
        elif i % 3 == 0:
            result.append("Fizz")
        elif i % 5 == 0:
            result.append("Buzz")
        else:
            result.append(str(i))
    return result

OUT = os.path.join(os.path.dirname(__file__), '..', 'fixtures', 'p412')
os.makedirs(OUT, exist_ok=True)

for n in range(1, 10001):
    with open(os.path.join(OUT, f'{n:05d}.in'),  'w') as f: f.write(f'{n}\n')
    with open(os.path.join(OUT, f'{n:05d}.out'), 'w') as f: f.write(json.dumps(fizz_buzz(n)) + '\n')

print('Generated 10000 fixtures in fixtures/p412/')
