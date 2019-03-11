""" Production Settings """

import os
from .dev import *


############
# SECURITY #
############

SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY')

DEBUG = False
# Set to your Domain here
ALLOWED_HOSTS = ['*']