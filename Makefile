install:
	poetry install

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install dist/*.whl

package-reinstall:
	python3 -m pip install dist/*.whl --force-reinstall

package-uninstall:
	python3 -m pip uninstall dist/*.whl

lint:
	poetry run flake8 scripts
