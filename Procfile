release: python manage.py migrate
web: gunicorn tushop.wsgi
release: python manage.py collectstatic
web: python manage.py runserver 0.0.0.0:$PORT --settings=tushop.settings
