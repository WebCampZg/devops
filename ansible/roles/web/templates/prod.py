from .base import *

DEBUG = False

ALLOWED_HOSTS = ['2015.webcampzg.org']

import dj_database_url

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTOCOL', 'https')
SESSION_EXPIRE_AT_BROWSER_CLOSE = True
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True

DATABASES = {'default': dj_database_url.config(
    default='postgres://{{ dbuser }}:{{ dbpassword }}@localhost:5432/{{ dbname }}'
)}

