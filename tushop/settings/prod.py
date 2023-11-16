# import os

import dj_database_url

from .common import *

DEBUG = True

SECRET_KEY = os.environ['SECRET_KEY']

ALLOWED_HOSTS = ['shoplify-prod-5de22bcffe74.herokuapp.com', 'shoplify-prod-231a968d6096.herokuapp.com']

DATABASES = {
    'default':dj_database_url.config()
}
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'qhx06luyg7dzctwo',
#         'HOST': 't07cxyau6qg7o5nz.cbetxkdyhwsb.us-east-1.rds.amazonaws.com',
#         'USER': 'jkjsk56die2h2f2b',
#         'PASSWORD': 'z70ae2d9dw7jprs4',
#         'PORT': 3306
#     }
# }