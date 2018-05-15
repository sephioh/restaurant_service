FROM python:3.6

RUN pip install pipenv

WORKDIR /app

COPY Pipfile /app/
COPY Pipfile.lock /app/

RUN pipenv install
