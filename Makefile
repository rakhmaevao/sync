format:
	poetry run isort .
	poetry run ruff format .

mypy:
	poetry run mypy main.py sync

run:
	poetry run python main.py