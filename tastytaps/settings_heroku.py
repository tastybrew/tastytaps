import dj_database_url

from .settings import *  # noqa


# Heroku overrides.
DATABASES = {'default': dj_database_url.config()}
SECRET_KEY = os.environ['DJANGO_SECRET']
