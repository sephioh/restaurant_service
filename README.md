# restaurant_service
An HTTP api service to manage restaurants.

# Requirements
* [docker](https://www.docker.com/)
* [docker-compose](https://docs.docker.com/compose/)
* make

# How to run
Start the application (inside a docker container) with this command:
```
make run
```

This will start the application at http://localhost:8000.

# Tests

## Acceptance Tests
Run acceptance tests with this command:
```
make acceptance_tests
```

## Unit Tests
Run unit tests with this command:
```
make unit_tests
```

## Lint
Run code quality ensurance tests using this command:
```
make lint
```

## Built with
* [Python](https://www.python.org/)
* [Django](https://www.djangoproject.com/)
* [Django REST framework](http://www.django-rest-framework.org/)
* [docker](https://www.docker.com/)
* [docker-compose](https://docs.docker.com/compose/)
* [behave-django](https://behave-django.readthedocs.io/en/stable/)
* [Django REST swagger](https://django-rest-swagger.readthedocs.io/en/latest/)
