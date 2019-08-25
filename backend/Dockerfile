from python:3

workdir /app

run pip install poetry

copy pyproject.toml .

copy poetry.lock .

run poetry install

copy util .

copy magic .
