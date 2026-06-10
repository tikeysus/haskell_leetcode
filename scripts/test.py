#!/usr/bin/env python3
"""
Usage: python3 scripts/test.py <problem>
  e.g. python3 scripts/test.py p509
"""
import subprocess, sys, os, glob, shutil, json

# ── ANSI ──────────────────────────────────────────────────────────────────────
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
def sep():     return dim('─' * 50)

# ── pipeline steps ────────────────────────────────────────────────────────────
def copy_submission(problem):
    src = os.path.join('submissions', f'{problem}.hs')
    dst = os.path.join(problem, 'Solution.hs')
    if not os.path.exists(src):
        print(f'\n  {red("error")}  submissions/{problem}.hs not found\n')
        sys.exit(1)
    shutil.copy2(src, dst)

def build(problem):
    result = subprocess.run(
        ['stack', 'build', f'haskell-leetcode:exe:{problem}'],
        capture_output=True, text=True
    )
    return result.returncode == 0, result.stderr

def get_binary(problem):
    result = subprocess.run(
        ['stack', 'path', '--local-install-root'],
        capture_output=True, text=True
    )
    return os.path.join(result.stdout.strip(), 'bin', problem)

def compare(actual, expected):
    if expected.startswith('['):
        try:
            return sorted(json.loads(actual)) == sorted(json.loads(expected))
        except Exception:
            pass
    return actual == expected

def run_case(binary, case_in, case_out):
    with open(case_in)  as f: inp      = f.read()
    with open(case_out) as f: expected = f.read().strip()
    try:
        result = subprocess.run(
            [binary], input=inp, capture_output=True, text=True, timeout=5
        )
        if result.returncode != 0:
            return 'crash', result.stderr.strip(), expected, inp.strip()
        actual = result.stdout.strip()
        return ('pass' if compare(actual, expected) else 'fail'), actual, expected, inp.strip()
    except subprocess.TimeoutExpired:
        return 'timeout', '', expected, inp.strip()

# ── output ────────────────────────────────────────────────────────────────────
def extract_ghc_errors(stderr):
    """Return only the GHC diagnostic lines, stripping Stack boilerplate."""
    lines = stderr.splitlines()
    # GHC output starts after the last "[N of M] Compiling" line
    start = 0
    for i, line in enumerate(lines):
        if '] Compiling' in line:
            start = i + 1
    # GHC output ends at the "Error: [S-" Stack footer
    end = len(lines)
    for i in range(start, len(lines)):
        if lines[i].startswith('Error: [S-'):
            end = i
            break
    return lines[start:end]

def show_compile_error(problem, stderr):
    abs_solution = os.path.abspath(os.path.join(problem, 'Solution.hs'))
    print(f'\n  {bold(problem)}  {red("compile error")}')
    print(f'  {sep()}')
    for line in extract_ghc_errors(stderr):
        line = line.replace(abs_solution, f'submissions/{problem}.hs')
        print(f'  {line}')
    print(f'  {sep()}')
    print(f'  {red(bold("build failed"))}\n')

# ── main ──────────────────────────────────────────────────────────────────────
def main():
    if len(sys.argv) < 2:
        print('usage: python3 scripts/test.py <problem>')
        sys.exit(1)

    problem = sys.argv[1]

    copy_submission(problem)

    print(f'\n  {bold(problem)}  {dim("building...")}', end='\r', flush=True)
    ok, stderr = build(problem)
    if not ok:
        show_compile_error(problem, stderr)
        sys.exit(1)

    binary      = get_binary(problem)
    fixture_dir = os.path.join('fixtures', problem)
    cases       = sorted(glob.glob(os.path.join(fixture_dir, '*.in')))

    if not cases:
        print(red(f'  no fixtures found in {fixture_dir}/'))
        sys.exit(1)

    print(f'  {bold(problem)}  {dim(str(len(cases)) + " cases")}          ')
    print(f'  {sep()}')

    passed, failed = 0, 0

    for case_in in cases:
        case_out = case_in.replace('.in', '.out')
        name     = os.path.basename(case_in).replace('.in', '')
        status, actual, expected, inp = run_case(binary, case_in, case_out)

        if status == 'pass':
            passed += 1
            print(f'  {green("✓")}  {dim(name)}  {dim(inp + "  →  " + actual)}')
        elif status == 'fail':
            failed += 1
            print(f'  {red("✗")}  {name}')
            print(f'       {dim("input")}     {inp}')
            print(f'       {dim("expected")}  {expected}')
            print(f'       {red("got")}       {red(actual)}')
        elif status == 'crash':
            failed += 1
            msg = actual[:120] if actual else '(no output)'
            print(f'  {red("✗")}  {name}  {yellow("runtime error")}')
            print(f'       {dim("input")}     {inp}')
            print(f'       {red("stderr")}    {red(msg)}')
        elif status == 'timeout':
            failed += 1
            print(f'  {red("✗")}  {name}  {yellow("timed out (>5s)")}')
            print(f'       {dim("input")}     {inp}')

    print(f'  {sep()}')
    if failed == 0:
        print(f'  {green(bold(f"all {passed} passed"))}')
    else:
        print(f'  {green(str(passed) + " passed")}  {dim("·")}  {red(bold(str(failed) + " failed"))}')
    print()
    sys.exit(0 if failed == 0 else 1)

if __name__ == '__main__':
    main()
