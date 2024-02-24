format:
	poetry run isort .
	poetry run ruff format .

lint:
	poetry run ruff lint backup.py sync.py src

mypy:
	poetry run mypy backup.py sync.py src

sync:
	poetry run python sync.py

backup:
	poetry run python backup.py
