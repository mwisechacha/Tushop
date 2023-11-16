import os
from .common import *
import dj_database_url

DEBUG = False

SECRET_KEY = os.environ['SECRET_KEY']

ALLOWED_HOSTS = ['shoplify-prod-231a968d6096.herokuapp.com']

DATABASES = {
    'default':dj_database_url.config()
}
