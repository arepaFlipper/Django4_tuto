#!/bin/sh

set -o errexit
set -o nounset

python /REST/backend/manage.py makemigrations
python /REST/backend/manage.py migrate
python /REST/backend/manage.py runserver 0.0.0.0:8000
