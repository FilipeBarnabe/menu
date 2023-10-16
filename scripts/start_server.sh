/root/.local/bin/poetry run python manage.py makemigrations

/root/.local/bin/poetry run python manage.py migrate

/root/.local/bin/poetry run python manage.py collectstatic

/root/.local/bin/poetry run gunicorn menu.wsgi:application --bind 0.0.0.0:8000