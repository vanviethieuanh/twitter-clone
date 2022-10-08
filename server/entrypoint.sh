#!/bin/bash

# echo "Collecting statics ..."
# python3 ./manage.py collectstatic --noinput

echo "Making migration ..."
python3 ./manage.py migrate

# Run uWSGI
uwsgi --ini /app/uwsgi.ini --module server.wsgi