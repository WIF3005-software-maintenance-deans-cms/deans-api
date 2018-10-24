#!/bin/bash
cd $DJANGO_ROOT
python3 manage.py collectstatic --no-input;
python3 manage.py makemigrations;
python3 manage.py migrate;
python3 manage.py loaddata $DATA_ROOT/users.json
python3 manage.py runserver 0.0.0.0:8000;
# gunicorn  --log-level=debug --bind :8000 deans_api.wsgi:application;
