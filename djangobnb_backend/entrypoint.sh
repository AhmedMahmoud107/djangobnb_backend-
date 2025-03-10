#!/bin/sh

if ["$DATABASE" = "postgres"] 
then
  echo "Check if databases is running..."

  while ! nc -z $SQL_HOST $SQL_PORT; do
    sleep 0.1
  done 

  echo "Check if databases is running :-D"
fi

python manage.py makemigrations
python manage.py migrate

exec "$@"
