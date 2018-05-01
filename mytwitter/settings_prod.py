import os
import dj_database_url
from .settings import *

DEBUG = os.environ.get('DEBUG', False)

SECRET_KEY = os.environ.get('SECRET_KEY')

ALLOWED_HOSTS = [
    'django-mytweet-sample.herokuapp.com'
]

DATABASES = {
    'default': dj_database_url.config(),
}
