import os

from purbeurre.settings import *

SECRET_KEY = os.environ.get('SECRET_KEY', '8fsm7s-poju5ht*%j$@__r8(orf%o=nvei1l9q#0v$^1w+pu8=')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'purbeurre',
        'USER': 'postgres',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    },
}
