# release: python manage.py migrate &&
# web: python server.py
release: python manage.py collectstatic
web: gunicorn tushop.wsgi
# web: python manage.py runserver 0.0.0.0:$PORT --settings=tushop.settings.prod
