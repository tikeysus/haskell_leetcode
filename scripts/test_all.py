#!/usr/bin/env python3
"""Run tests for all submissions, skipping problems that already passed with the same source."""
import glob, hashlib, json, os, subprocess, sys
from datetime import datetime, timezone

RESET  = '\033[0m'
BOLD   = '\033[1m'
DIM    = '\033[2m'
GREEN  = '\033[32m'
RED    = '\033[31m'
YELLOW = '\033[33m'

def bold(s):   return f'{BOLD}{s}{RESET}'
def dim(s):    return f'{DIM}{s}{RESET}'
def green(s):  return f'{GREEN}{s}{RESET}'
def red(s):    return f'{RED}{s}{RESET}'
def yellow(s): return f'{YELLOW}{s}{RESET}'

CACHE_PATH = '.test_cache.json'

def load_cache():
    try:
        with open(CACHE_PATH) as f:
            return json.load(f)
    except (OSError, json.JSONDecodeError):
        return {}

def save_cache(cache):
    with open(CACHE_PATH, 'w') as f:
        json.dump(cache, f, indent=2)
        f.write('\n')

def file_hash(path):
    h = hashlib.sha256()
    with open(path, 'rb') as f:
        h.update(f.read())
    return h.hexdigest()

def main():
    problems = sorted(
        os.path.basename(p).replace('.hs', '')
        for p in glob.glob(os.path.join('submissions', 'p*.hs'))
    )
    if not problems:
        print(red('no submissions found'))
        sys.exit(1)

    cache = load_cache()
    passed = failed = skipped = 0

    for problem in problems:
        src = os.path.join('submissions', f'{problem}.hs')
        h = file_hash(src)
        entry = cache.get(problem, {})

        if entry.get('hash') == h and entry.get('passed'):
            print(f'  {dim("·")}  {dim(problem)}  {dim("cached ✓")}')
            skipped += 1
            continue

        result = subprocess.run(
            [sys.executable, 'scripts/test.py', problem],
            text=True
        )
        ok = result.returncode == 0
        cache[problem] = {
            'hash': h,
            'passed': ok,
            'timestamp': datetime.now(timezone.utc).isoformat(),
        }
        save_cache(cache)
        if ok:
            passed += 1
        else:
            failed += 1

    print()
    parts = []
    if passed:  parts.append(green(f'{passed} passed'))
    if failed:  parts.append(red(bold(f'{failed} failed')))
    if skipped: parts.append(dim(f'{skipped} skipped'))
    print('  ' + dim('─' * 50))
    print('  ' + '  ·  '.join(parts))
    print()
    sys.exit(0 if failed == 0 else 1)

if __name__ == '__main__':
    main()
