#!/usr/bin/env python3
"""Unit tests for scripts/test.py — run with: python3 scripts/test_harness.py"""
import importlib.util, os, sys, stat, tempfile, unittest

# ── load test.py as a module without triggering __main__ ──────────────────────
_spec = importlib.util.spec_from_file_location(
    "_runner",
    os.path.join(os.path.dirname(os.path.abspath(__file__)), "test.py"),
)
_mod = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_mod)

compare     = _mod.compare
run_batch   = _mod.run_batch
get_timeout = _mod.get_timeout


# ── helpers ───────────────────────────────────────────────────────────────────
def _make_fixture(directory, name, content):
    path = os.path.join(directory, name)
    with open(path, "w") as f:
        f.write(content)
    return path

def _make_binary(directory, script):
    """Write an executable Python script and return its path (a string)."""
    path = os.path.join(directory, "fake_binary.py")
    with open(path, "w") as f:
        f.write("#!/usr/bin/env python3\nimport sys\n" + script)
    os.chmod(path, os.stat(path).st_mode | stat.S_IEXEC)
    return path


# ── compare ───────────────────────────────────────────────────────────────────
class TestCompare(unittest.TestCase):
    def test_equal_strings(self):
        self.assertTrue(compare("hello", "hello"))

    def test_unequal_strings(self):
        self.assertFalse(compare("hello", "world"))

    def test_json_list_order_insensitive(self):
        self.assertTrue(compare("[3,1,2]", "[1,2,3]"))

    def test_json_list_unequal(self):
        self.assertFalse(compare("[1,2]", "[1,2,3]"))

    def test_json_list_of_lists_order_insensitive(self):
        self.assertTrue(compare("[[3,4],[1,2]]", "[[1,2],[3,4]]"))

    def test_invalid_json_falls_back_to_string(self):
        self.assertTrue(compare("[broken", "[broken"))
        self.assertFalse(compare("[broken", "[other"))

    def test_int_output(self):
        self.assertTrue(compare("42", "42"))
        self.assertFalse(compare("42", "43"))


# ── run_batch ─────────────────────────────────────────────────────────────────
class TestRunBatch(unittest.TestCase):
    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.d = self._tmp.name

    def tearDown(self):
        self._tmp.cleanup()

    # ── normal operation ──────────────────────────────────────────────────────
    def test_normal_run_returns_one_line_per_case(self):
        cases = [
            _make_fixture(self.d, "0.in", "1\n"),
            _make_fixture(self.d, "1.in", "2\n"),
            _make_fixture(self.d, "2.in", "3\n"),
        ]
        binary = _make_binary(self.d, "for line in sys.stdin: print(int(line.strip()) * 10)\n")
        rc, lines, stderr, elapsed = run_batch(binary, cases, 5.0)
        self.assertEqual(rc, 0)
        self.assertEqual(lines, ["10", "20", "30"])

    def test_elapsed_is_non_negative(self):
        cases = [_make_fixture(self.d, "0.in", "x\n")]
        binary = _make_binary(self.d, "for line in sys.stdin: print(line.strip())\n")
        _, _, _, elapsed = run_batch(binary, cases, 5.0)
        self.assertGreaterEqual(elapsed, 0.0)

    def test_multi_line_fixture_chunked_correctly(self):
        """Two-arg problem: each case is two lines; three cases = six lines total."""
        cases = [
            _make_fixture(self.d, "0.in", "1\n2\n"),
            _make_fixture(self.d, "1.in", "3\n4\n"),
            _make_fixture(self.d, "2.in", "5\n6\n"),
        ]
        # Binary reads pairs of lines and sums them
        script = (
            "lines = [l.strip() for l in sys.stdin if l.strip()]\n"
            "pairs = [(lines[i], lines[i+1]) for i in range(0, len(lines), 2)]\n"
            "for a, b in pairs: print(int(a) + int(b))\n"
        )
        binary = _make_binary(self.d, script)
        rc, lines, _, _ = run_batch(binary, cases, 5.0)
        self.assertEqual(rc, 0)
        self.assertEqual(lines, ["3", "7", "11"])

    # ── missing trailing newline ───────────────────────────────────────────────
    def test_fixture_without_trailing_newline_is_not_joined_to_next(self):
        """A fixture missing its final \\n must not concatenate with the next fixture."""
        cases = [
            _make_fixture(self.d, "0.in", "hello"),   # no trailing newline
            _make_fixture(self.d, "1.in", "world\n"),
        ]
        binary = _make_binary(self.d, "for line in sys.stdin: print(line.strip())\n")
        rc, lines, _, _ = run_batch(binary, cases, 5.0)
        self.assertEqual(rc, 0)
        self.assertEqual(lines, ["hello", "world"])

    # ── crash detection ───────────────────────────────────────────────────────
    def test_crash_returns_nonzero_rc(self):
        cases = [_make_fixture(self.d, "0.in", "x\n")]
        binary = _make_binary(self.d, "sys.exit(1)\n")
        rc, lines, stderr, _ = run_batch(binary, cases, 5.0)
        self.assertNotEqual(rc, 0)

    def test_crash_after_partial_output(self):
        """Binary that produces output for case 0 then crashes before case 1."""
        cases = [
            _make_fixture(self.d, "0.in", "a\n"),
            _make_fixture(self.d, "1.in", "b\n"),
        ]
        script = (
            "lines = list(sys.stdin)\n"
            "print(lines[0].strip())\n"
            "sys.exit(2)\n"
        )
        binary = _make_binary(self.d, script)
        rc, lines, _, _ = run_batch(binary, cases, 5.0)
        self.assertNotEqual(rc, 0)
        self.assertEqual(lines, ["a"])   # only one line produced

    def test_crash_with_stderr(self):
        cases = [_make_fixture(self.d, "0.in", "x\n")]
        binary = _make_binary(self.d, "sys.stderr.write('boom\\n'); sys.exit(1)\n")
        rc, lines, stderr, _ = run_batch(binary, cases, 5.0)
        self.assertNotEqual(rc, 0)
        self.assertIn("boom", stderr)

    # ── extra output lines ────────────────────────────────────────────────────
    def test_extra_output_lines_are_returned(self):
        """run_batch itself returns raw lines; caller is responsible for detecting extras."""
        cases = [_make_fixture(self.d, "0.in", "x\n")]
        binary = _make_binary(self.d, "print('a'); print('b'); print('c')\n")
        rc, lines, _, _ = run_batch(binary, cases, 5.0)
        self.assertEqual(rc, 0)
        self.assertEqual(len(lines), 3)   # 2 extra

    # ── timeout ───────────────────────────────────────────────────────────────
    def test_timeout_returns_none_rc(self):
        cases = [_make_fixture(self.d, "0.in", "x\n")]
        binary = _make_binary(self.d, "import time; time.sleep(10)\n")
        rc, lines, _, elapsed = run_batch(binary, cases, 0.1)
        self.assertIsNone(rc)
        self.assertEqual(lines, [])

    def test_timeout_elapsed_reflects_actual_wait(self):
        cases = [_make_fixture(self.d, "0.in", "x\n")]
        binary = _make_binary(self.d, "import time; time.sleep(10)\n")
        _, _, _, elapsed = run_batch(binary, cases, 0.2)
        self.assertGreaterEqual(elapsed, 0.2)


# ── get_timeout ───────────────────────────────────────────────────────────────
class TestGetTimeout(unittest.TestCase):
    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self._orig_dir = os.getcwd()
        os.chdir(self._tmp.name)

    def tearDown(self):
        os.chdir(self._orig_dir)
        self._tmp.cleanup()

    def _make_timeout_file(self, problem, value):
        d = os.path.join("fixtures", problem)
        os.makedirs(d, exist_ok=True)
        with open(os.path.join(d, ".timeout"), "w") as f:
            f.write(str(value) + "\n")

    def test_returns_default_when_file_absent(self):
        self.assertEqual(get_timeout("p_no_such"), 60.0)

    def test_reads_custom_timeout(self):
        self._make_timeout_file("p_slow", "120")
        self.assertEqual(get_timeout("p_slow"), 120.0)

    def test_fractional_timeout(self):
        self._make_timeout_file("p_fast", "0.5")
        self.assertEqual(get_timeout("p_fast"), 0.5)

    def test_returns_default_on_invalid_content(self):
        d = os.path.join("fixtures", "p_bad")
        os.makedirs(d, exist_ok=True)
        with open(os.path.join(d, ".timeout"), "w") as f:
            f.write("not_a_number\n")
        self.assertEqual(get_timeout("p_bad"), 60.0)


if __name__ == "__main__":
    unittest.main(verbosity=2)
