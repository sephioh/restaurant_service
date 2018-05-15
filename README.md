# restaurant_service
An HTTP api service to manage restaurants.

# Requirements
* docker
* docker-compose

# How to run
Start the application (inside a docker container) with this command:
```
docker-compose up
```

This will start the application at http://localhost:8000.


# Tests

## Acceptance Tests
Run acceptance tests with this command:
```
docker-compose run app pipenv run python manage.py behave
```

## Unit Tests
Run unit tests with this command:
```
docker-compose run app pipenv run python manage.py test
```
