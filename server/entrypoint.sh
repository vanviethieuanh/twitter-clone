#!/bin/bash

echo "Collecting static ..."
python3 ./manage.py collectstatic

echo "Making migration ..."
python3 ./manage.py migrate

# Run uWSGI
uwsgi --ini /app/uwsgi.ini --module server.wsgi