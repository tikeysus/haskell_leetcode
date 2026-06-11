fixtures-%:
	@python3 scripts/gen_$*.py

test-%:
	@python3 scripts/test.py $*

lint:
	@python3 scripts/lint.py

test-harness:
	@python3 scripts/test_harness.py
