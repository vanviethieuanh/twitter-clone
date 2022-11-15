#!/bin/bash

echo "Collecting static ..."
python3 ./manage.py collectstatic --no-input

echo "Making migration ..."
python3 ./manage.py migrate --no-input

echo "Creating superuser ..."
python3 ./manage.py createsuperuser --username admin --email admin@example.com --no-input

# Run uWSGI
uwsgi --ini /app/uwsgi.ini --module server.wsgi