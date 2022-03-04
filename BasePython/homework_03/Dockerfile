# To build run:             docker build . -t hw03app
# To run container run:     docker run -it -p 8000:8000 hw03app


FROM python:3.9-buster

ENV PYTHONBUFFERED=1

WORKDIR /app

RUN pip install poetry
RUN poetry config virtualenvs.create false

COPY ./pyproject.toml ./pyproject.toml
COPY ./poetry.lock ./poetry.lock

RUN poetry install --no-dev --no-ansi

COPY . .

EXPOSE 8000
CMD uvicorn main:app --host 0.0.0.0 --port 8000
