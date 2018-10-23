#!/bin/bash

python manage.py collectstatic --no-input &&\
python3 manage.py makemigrations &&\
python3 manage.py migrate &&\
python3 manage.py runserver 0.0.0.0:8000
# gunicorn --chdir deans_api --log-level=debug --bind :8000 deans_api.wsgi:application
