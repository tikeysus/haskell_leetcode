#!/usr/bin/env python3
"""
Usage: python3 scripts/test.py <problem>
       python3 scripts/test.py all
  e.g. python3 scripts/test.py p509
"""
import subprocess, sys, os, glob, shutil, json, hashlib, time
from datetime import datetime, timezone

CACHE_FILE = '.test_cache.json'

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

# ── cache ─────────────────────────────────────────────────────────────────────
def compute_hash(problem):
    """SHA256 of submission file + all fixture files (sorted)."""
    h = hashlib.sha256()
    src = os.path.join('submissions', f'{problem}.hs')
    with open(src, 'rb') as f: h.update(f.read())
    for path in sorted(glob.glob(os.path.join('fixtures', problem, '*'))):
        with open(path, 'rb') as f: h.update(f.read())
    return h.hexdigest()

def load_cache():
    if os.path.exists(CACHE_FILE):
        with open(CACHE_FILE) as f:
            return json.load(f)
    return {}

def save_cache(cache):
    with open(CACHE_FILE, 'w') as f:
        json.dump(cache, f, indent=2)

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

def get_timeout(problem):
    path = os.path.join('fixtures', problem, '.timeout')
    try:
        with open(path) as f:
            return float(f.read().strip())
    except (OSError, ValueError):
        return 60.0

def run_batch(binary, cases, timeout):
    """Concatenate all fixture inputs and run binary once. Returns (returncode, output_lines, stderr, elapsed)."""
    parts = []
    for case_in in cases:
        with open(case_in) as f:
            content = f.read()
        if not content.endswith('\n'):
            content += '\n'
        parts.append(content)
    all_input = ''.join(parts)
    t0 = time.monotonic()
    try:
        result = subprocess.run(
            [binary], input=all_input, capture_output=True, text=True, timeout=timeout
        )
        return result.returncode, result.stdout.splitlines(), result.stderr, time.monotonic() - t0
    except subprocess.TimeoutExpired:
        return None, [], '', time.monotonic() - t0

# ── output ────────────────────────────────────────────────────────────────────
def extract_ghc_errors(stderr):
    """Return only the GHC diagnostic lines, stripping Stack boilerplate."""
    lines = stderr.splitlines()
    start = 0
    for i, line in enumerate(lines):
        if '] Compiling' in line:
            start = i + 1
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

# ── test one problem ──────────────────────────────────────────────────────────
def test_problem(problem):
    """Run all fixtures for one problem. Returns (passed, failed, skipped)."""
    copy_submission(problem)

    print(f'\n  {bold(problem)}  {dim("building...")}', end='\r', flush=True)
    ok, stderr = build(problem)
    if not ok:
        show_compile_error(problem, stderr)
        return 0, 0, 1

    binary      = get_binary(problem)
    fixture_dir = os.path.join('fixtures', problem)
    cases       = sorted(glob.glob(os.path.join(fixture_dir, '*.in')))

    if not cases:
        print(red(f'  no fixtures found in {fixture_dir}/'))
        return 0, 0, 1

    timeout = get_timeout(problem)
    print(f'  {bold(problem)}  {dim(str(len(cases)) + " cases")}          ')
    print(f'  {sep()}')

    rc, output_lines, run_stderr, elapsed = run_batch(binary, cases, timeout)

    if rc is None:
        print(f'  {red("✗")}  {yellow(f"timed out (>{timeout:.0f}s) running all cases")}')
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
    timing = dim(f'{elapsed:.2f}s')
    if failed == 0:
        print(f'  {green(bold(f"all {passed} passed"))}  {timing}')
    else:
        print(f'  {green(str(passed) + " passed")}  {dim("·")}  {red(bold(str(failed) + " failed"))}  {timing}')
    print()
    return passed, failed, 0

# ── main ──────────────────────────────────────────────────────────────────────
def main():
    if len(sys.argv) < 2:
        print('usage: python3 scripts/test.py <problem|all>')
        sys.exit(1)

    arg = sys.argv[1]

    if arg != 'all':
        _, failed, skipped = test_problem(arg)
        sys.exit(0 if failed == 0 and skipped == 0 else 1)

    # discover all submissions
    paths    = sorted(glob.glob(os.path.join('submissions', 'p*.hs')))
    problems = [os.path.basename(p).replace('.hs', '') for p in paths]

    if not problems:
        print(red('  no submissions found'))
        sys.exit(1)

    cache = load_cache()

    total_passed  = 0
    total_failed  = 0
    total_skipped = 0
    problem_results = []  # (problem, p, f, s, cached)

    for problem in problems:
        digest = compute_hash(problem)
        entry  = cache.get(problem, {})

        if entry.get('hash') == digest and entry.get('passed'):
            n = entry.get('cases', '?')
            print(f'  {bold(problem)}  {dim("cached")}  {green(f"all {n} passed")}')
            total_passed += entry.get('cases', 0)
            problem_results.append((problem, entry.get('cases', 0), 0, 0, True))
            continue

        p, f, s = test_problem(problem)
        total_passed  += p
        total_failed  += f
        total_skipped += s

        cache[problem] = {
            'hash':      digest,
            'passed':    (f == 0 and s == 0),
            'cases':     p + f,
            'timestamp': datetime.now(timezone.utc).isoformat(),
        }
        save_cache(cache)

        problem_results.append((problem, p, f, s, False))

    # summary
    print(f'\n  {bold("═" * 48)}')
    print(f'  {bold("summary")}  {dim(str(len(problems)) + " problems")}')
    print(f'  {dim("─" * 48)}')
    for problem, p, f, s, cached in problem_results:
        tag = dim(' (cached)') if cached else ''
        if s:
            status = yellow('build error')
        elif f:
            status = red(f'{f} failed')
        else:
            status = green(f'all {p} passed')
        print(f'  {bold(problem):<12}  {status}{tag}')
    print(f'  {dim("─" * 48)}')
    print(f'  fixtures  {green(str(total_passed) + " passed")}', end='')
    if total_failed:
        print(f'  {dim("·")}  {red(bold(str(total_failed) + " failed"))}', end='')
    if total_skipped:
        print(f'  {dim("·")}  {yellow(str(total_skipped) + " skipped")}', end='')
    print(f'\n  {bold("═" * 48)}\n')

    sys.exit(0 if total_failed == 0 and total_skipped == 0 else 1)

if __name__ == '__main__':
    main()
