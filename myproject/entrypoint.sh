#!/bin/bash
cd /usr/src/app/plookjing
python manage.py migrate
python manage.py runserver 0.0.0.0:8000
