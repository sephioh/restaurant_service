run:
	docker-compose up

stop:
	docker-compose stop

acceptance_tests:
	docker-compose run app python3 manage.py behave

unit_tests:
	docker-compose run app python3 manage.py test

lint:
	docker-compose run app flake8

coverage:
	docker-compose run app coverage report
