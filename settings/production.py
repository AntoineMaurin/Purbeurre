import django_heroku
import os
import sentry_sdk

from sentry_sdk.integrations.django import DjangoIntegration

from purbeurre.settings import *


sentry_sdk.init(
    dsn="https://b936de09f9fd4340a40b0f77aaede1c2@o417103.ingest.sentry.io/5315293",
    integrations=[DjangoIntegration()],

    # If you wish to associate users to errors (assuming you are using
    # django.contrib.auth) you may enable sending PII data.
    send_default_pii=True
)

SECRET_KEY = os.environ['SECRET_KEY']

DEBUG = False

ALLOWED_HOSTS = ["46.101.184.139", ".herokuapps.com"]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'purbeurre',
        'USER': os.environ['DB_USER'],
        'PASSWORD': os.environ['DB_PASSWORD'],
        'HOST': os.environ['DB_HOST'],
        'PORT': os.environ['DB_PORT'],
    }
}

django_heroku.settings(locals())
