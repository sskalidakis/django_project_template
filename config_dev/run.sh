#!/usr/bin/env bash
#This file uses the container's environment variables found in .env_app_dev
echo 'Waiting for Postgres...'
while ! nc -z ${SQL_HOST} 5432; do
  sleep 0.1
done

#These lines have been commented out since they delete everything in the database each time the container is recreated
#echo 'COMPLETELY Clearing the database...'
#python manage.py flush --no-input

echo 'Applying migrations...'
python manage.py migrate

echo 'Collecting static files...'
python manage.py collectstatic --noinput --settings=${SETTINGS}

echo "Run Gunicorn"
python manage.py runserver 0:${PORT} --settings=${SETTINGS}

