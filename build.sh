#!/usr/bin/env bash
# exit on error
set -o errexit

python manage.py collectstatic --no-input

python manage.py makemigrations
python manage.py migrate