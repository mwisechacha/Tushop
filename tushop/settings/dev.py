import dj_database_url

from .common import *

DEBUG = True
SECRET_KEY = 'django-insecure-920ltosg7!q)ailxpkji%av^&s)na7p_*eg2(omy=e+109*=+7'


# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'tushop',
#         'HOST': 'localhost',
#         'USER': 'root',
#         'PASSWORD': 'rootkristine'
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'qhx06luyg7dzctwo',
        'HOST': 't07cxyau6qg7o5nz.cbetxkdyhwsb.us-east-1.rds.amazonaws.com',
        'USER': 'jkjsk56die2h2f2b',
        'PASSWORD': 'z70ae2d9dw7jprs4',
        'PORT': 3306
        }
}