""" Production Settings """

import os

import dj_database_url

from .dev import *


############
# DATABASE #
############
DATABASES = {
    'default': dj_database_url.config(
        default=os.getenv('DATABASE_URL')
    )
}

############
# SECURITY #
############

SECRET_KEY = os.getenv('DJANGO_SECRET_KEY')

DEBUG = False
# Set to your Domain here
ALLOWED_HOSTS = ['*']