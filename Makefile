format:
	isort .
	black .

mypy:
	mypy .

run:
	poetry run python main.py