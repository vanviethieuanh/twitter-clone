#!/bin/bash

echo "Collecting static ..."
python3 ./manage.py collectstatic

echo "Making migration ..."
python3 ./manage.py migrate

echo "Creating superuser ..."
python3 ./manage.py createsuperuser --username admin --no-input

# Run uWSGI
uwsgi --ini /app/uwsgi.ini --module server.wsgi