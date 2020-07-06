import django_heroku

from purbeurre.settings import *

SECRET_KEY = "t-l@zgp9zyog3t%j5ee)1rqd600_(u9mz@b_8$bkohr@3d7@on"

DEBUG = False

ALLOWED_HOSTS = "46.101.184.139"

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        # 'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        'NAME': 'purbeurre',
        'USER': 'user_purbeurre',
        'PASSWORD': 'elpassword',
        'HOST': 'localhost',
        'PORT': '5432'
    }
}

django_heroku.settings(locals())
