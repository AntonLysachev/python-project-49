install:
		poerty install

brain-games:
		poetry run brain-games

build:
		poetry build

publish:
		poetry publish --dry-run

package-install:
		python3 -m pip install --user dist/hexlet_code-0.4.0-py3-none-any.whl

lint:
		poetry run flake8 brain_games
