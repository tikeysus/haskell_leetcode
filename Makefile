fixtures-%:
	@python3 scripts/gen_$*.py

test-%:
	@python3 scripts/test.py $*
