from .common import *

DEBUG = True
SECRET_KEY = 'django-insecure-920ltosg7!q)ailxpkji%av^&s)na7p_*eg2(omy=e+109*=+7'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'tushop',
        'HOST': 'localhost',
        'USER': 'root',
        'PASSWORD': 'rootkristine'
    }
}
