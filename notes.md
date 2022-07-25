docker build .
docker-compose build <!--! display a docker environment -->

# Migrations

docker volume ls <!--! display all volumes -->
docker volume rm _name of the volume_ <!--! remove volume --> <!- if does not allow, clear containers -->

# Unit test command :

docker-compose run --rm app sh -c "flake8" <!--! Run linter -->
docker-compose run --rm app sh -c "python manage.py test" <!--! Run tests -->

docker-compose run --rm app sh -c "django-admin startproject app ." <!--! Create django project in the app dir -->
docker-compose run --rm app sh -c "python manage.py startapp core"
docker-compose run --rm app sh -c "python manage.py wait_for_db" <!--! Docker compose for running wait_for_db function -->
docker-compose run --rm app sh -c "python manage.py makemigrations" <!--! Docker compose for running wait_for_db function -->

docker-compose up <!--! Docker compose for starting services -->
docker-compose down <!--! Docker compose for clearing containers -->
TTD basics:

- write a test for a function.
- check if the test doesn't pass.
- write the function .
- check if the test passes.
