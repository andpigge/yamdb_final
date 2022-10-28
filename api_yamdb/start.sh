#!/bin/bash
python3 manage.py makemigrations reviews
python3 manage.py migrate
python3 manage.py collectstatic --no-input
gunicorn api_yamdb.wsgi:application --bind 0:8000
