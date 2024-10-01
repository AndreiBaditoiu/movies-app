#!/usr/bin/env bash
# exit on error
set -o errxit

pip install -r requirements.txt
python manage.py collectstatic --no-input
python manage.py migrate