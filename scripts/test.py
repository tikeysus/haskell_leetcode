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
    dst = os.path.join('problems', problem, 'Solution.hs')
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

def run_batch(binary, cases):
    """Concatenate all fixture inputs and run binary once. Returns (returncode, output_lines, stderr)."""
    parts = []
    for case_in in cases:
        with open(case_in) as f:
            content = f.read()
        if not content.endswith('\n'):
            content += '\n'
        parts.append(content)
    all_input = ''.join(parts)
    try:
        result = subprocess.run(
            [binary], input=all_input, capture_output=True, text=True, timeout=60
        )
        return result.returncode, result.stdout.splitlines(), result.stderr
    except subprocess.TimeoutExpired:
        return None, [], ''

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
    abs_solution = os.path.abspath(os.path.join('problems', problem, 'Solution.hs'))
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

    rc, output_lines, run_stderr = run_batch(binary, cases)

    if rc is None:
        print(f'  {red("✗")}  {yellow("timed out (>60s) running all cases")}')
        print(f'  {sep()}')
        print(f'  {red(bold(str(len(cases)) + " failed"))}')
        print()
        sys.exit(1)

    passed, failed = 0, 0

    for i, case_in in enumerate(cases):
        case_out = case_in.replace('.in', '.out')
        name     = os.path.basename(case_in).replace('.in', '')
        with open(case_in)  as f: inp      = f.read().strip()
        with open(case_out) as f: expected = f.read().strip()

        if i >= len(output_lines):
            # Binary crashed before producing this output line
            failed += 1
            print(f'  {red("✗")}  {name}  {yellow("no output (crash?)")}')
            if run_stderr and i == len(output_lines):
                msg = run_stderr.strip()[:120]
                print(f'       {red("stderr")}    {red(msg)}')
            continue

        actual = output_lines[i].strip()
        if compare(actual, expected):
            passed += 1
            display_inp = inp.replace('\n', '  ')
            print(f'  {green("✓")}  {dim(name)}  {dim(display_inp + "  →  " + actual)}')
        else:
            failed += 1
            display_inp = inp.replace('\n', '  ')
            print(f'  {red("✗")}  {name}')
            print(f'       {dim("input")}     {display_inp}')
            print(f'       {dim("expected")}  {expected}')
            print(f'       {red("got")}       {red(actual)}')

    # Extra output lines mean the binary emitted more than one line per case
    extra = len(output_lines) - len(cases)
    if extra > 0:
        failed += extra
        print(f'  {red("✗")}  {yellow(f"{extra} unexpected extra output line(s) detected")}')
        for line in output_lines[len(cases):len(cases) + 5]:
            print(f'       {red(repr(line))}')

    # Show rc != 0 stderr once if we haven't shown it yet
    if rc != 0 and run_stderr and len(output_lines) >= len(cases):
        print(f'  {yellow("binary exited non-zero")}')
        print(f'  {red(run_stderr.strip()[:240])}')

    print(f'  {sep()}')
    if failed == 0:
        print(f'  {green(bold(f"all {passed} passed"))}')
    else:
        print(f'  {green(str(passed) + " passed")}  {dim("·")}  {red(bold(str(failed) + " failed"))}')
    print()
    sys.exit(0 if failed == 0 else 1)

if __name__ == '__main__':
    main()
