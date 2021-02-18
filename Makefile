.PHONY: clean test package

clean:
	rm -rf build dist pesel.egg-info

test:
	pytest --cov-report --cov=pesel tests/

package:
	python setup.py sdist bdist_wheel