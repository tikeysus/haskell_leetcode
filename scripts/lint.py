#!/usr/bin/env python3
"""Verify all problems/*/Main.hs use batch I/O (interact or getContents)."""
import glob, sys

OLD_PATTERNS = ['readLn >>=', 'getLine >>=']

errors = []
for path in sorted(glob.glob('problems/*/Main.hs')):
    with open(path) as f:
        src = f.read()
    if 'interact' not in src and 'getContents' not in src:
        errors.append(path)
    else:
        hits = [p for p in OLD_PATTERNS if p in src]
        if hits:
            errors.append(f'{path} (contains old-style pattern: {hits[0]!r})')

if errors:
    print('ERROR: old-style single-case I/O detected:')
    for e in errors:
        print(f'  {e}')
    sys.exit(1)

total = len(glob.glob('problems/*/Main.hs'))
print(f'OK: all {total} Main.hs files use batch I/O')
