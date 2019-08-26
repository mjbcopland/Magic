from python:3.7

workdir /app

run pip install poetry

run poetry config settings.virtualenvs.in-project true

copy pyproject.toml .

copy poetry.lock .

run poetry install

copy . .

cmd poetry run python manage.py runserver 0:8000
