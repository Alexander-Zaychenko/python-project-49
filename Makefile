install:
	poetry install

brain-games:
	poetry run brain-games

publish:
	poetry publish --dry-run

build:
	poetry build

package-install:
	python3 -m pip install --user dist/*.whl --force