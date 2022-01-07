web: gunicorn lattices.wsgi
web: gunicorn hello:app
release: python manage.py makemigrations --noinput
release: python manage.py collectstatic --noinput
release: python manage.py migrate --noinput