.PHONY: clean test package

clean:
	rm -rf dist

test:
	poetry run pytest --cov-report term-missing --cov=pesel tests/

package:
	poetry build
