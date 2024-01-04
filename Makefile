format:
	poetry run isort .
	poetry run ruff format .

lint:
	poetry run ruff lint .

mypy:
	poetry run mypy main.py sync

run:
	poetry run python main.py