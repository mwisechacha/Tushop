# import os

import dj_database_url

from .common import *

DEBUG = True

SECRET_KEY = os.environ['SECRET_KEY']

ALLOWED_HOSTS = ['shoplify-prod-5de22bcffe74.herokuapp.com', 'shoplify-prod-231a968d6096.herokuapp.com']

DATABASES = {
    'default':dj_database_url.config()
}