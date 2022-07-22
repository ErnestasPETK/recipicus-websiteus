docker build .
docker-compose build

Unit test command :
docker-compose run --rm app sh -c "flake8" <!--! Run linter -->
docker-compose run --rm app sh -c "python manage.py test" <!--! Run tests -->

docker-compose run --rm app sh -c "django-admin startproject app ." <!--! Create django project in the app dir -->
docker-compose run --rm app sh -c "python manage.py startapp core"

docker-compose up <!--! Docker compose for starting services -->
docker-compose down <!--! Docker compose for destroying images -->
TTD basics:

- write a test for a function.
- check if the test doesn't pass.
- write the function .
- check if the test passes.
