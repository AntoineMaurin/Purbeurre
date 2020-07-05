from dotenv import load_dotenv

import os

import django_heroku

from purbeurre.settings import *

load_dotenv()

SECRET_KEY = os.environ['SECRET_KEY']

DEBUG = False

if os.environ['ALLOWED_HOSTS'] == '.herokuapps.com':
    django_heroku.settings(locals())

ALLOWED_HOSTS = os.environ['ALLOWED_HOSTS']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        # 'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        'NAME': 'purbeurre',
        'USER': os.environ['DB_USER'],
        'PASSWORD': os.environ['DB_PASSWORD'],
        'HOST': os.environ['DB_HOST'],
        'PORT': os.environ['DB_PORT'],
    }
}
