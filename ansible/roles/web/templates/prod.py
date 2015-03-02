from .base import *

DEBUG = False

ALLOWED_HOSTS = ['2015.webcampzg.org']

import dj_database_url
DATABASES = {'default': dj_database_url.config(
    default='postgres://{{ dbuser }}:{{ dbpassword }}@localhost:5432/{{ dbname }}'
)}

