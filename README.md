# DockerSetUp
#### Create clone:

```
https://github.com/vladislin/inforce-test-task.git
```

#### Create at the root of the project file `.env`, example:

```
SECRET_KEY=change_me
DEBUG=1
DJANGO_ALLOWED_HOSTS=*
DB_ENGINE=django.db.backends.postgresql
POSTGRES_DB=db_name
POSTGRES_USER=postgres
POSTGRES_PASSWORD=password
DB_HOST=db
DB_PORT=5432
```

#### Up docker-compose:

```
docker-compose up
```

#### To view endpoints go to: http://localhost:8000/swagger/

#### Create superuser:

```
docker-compose run web python manage.py createsuperuser
```
