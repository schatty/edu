FROM python:3.9.9-buster

ENV PYTHONBUFFERED=1

WORKDIR /app

RUN pip install poetry
RUN poetry config virtualenvs.create false

COPY ./pyproject.toml ./pyproject.toml
COPY ./poetry.lock ./poetry.lock

RUN poetry install --no-dev --no-ansi

COPY . .

CMD uvicorn main:app --host 0.0.0.0 --port 8000