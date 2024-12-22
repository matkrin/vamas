default:
	just --list

lint:
    uv run ruff check vamas

test:
	uv run pytest

typecheck:
	uv run mypy -p vamas

typecheck-all:
	uv run mypy .

format-check:
	uv run ruff format --check .

format:
	uv run ruff format .
