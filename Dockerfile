FROM python:3.6-alpine

RUN pip install pipenv

WORKDIR /app

COPY Pipfile /app/
COPY Pipfile.lock /app/
COPY restaurant_service /app/

EXPOSE 8000

RUN pipenv install --dev --system --deploy
