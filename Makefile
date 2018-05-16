run:
	docker-compose up

stop:
	docker-compose stop

acceptance_tests:
	docker-compose run app pipenv run python manage.py behave

unit_tests:
	docker-compose run app pipenv run python manage.py test

lint:
	docker-compose run app pipenv run flake8
