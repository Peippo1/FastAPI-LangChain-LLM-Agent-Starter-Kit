.PHONY: install run dev test docker-build docker-up docker-down

install:
\tpython -m venv .venv
\t. .venv/bin/activate && pip install --upgrade pip && pip install -r requirements.txt

run:
\t. .venv/bin/activate && uvicorn app.main:app --reload --port 8000

dev: run

test:
\t. .venv/bin/activate && pytest

docker-build:
\tdocker build -t llm-agent-starter .

docker-up:
\tdocker-compose up --build

docker-down:
\tdocker-compose down