from .base import *
import dj_database_url

DEBUG = False

ALLOWED_HOSTS = ['2015.webcampzg.org', '128.199.33.243']

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTOCOL', 'https')
SESSION_EXPIRE_AT_BROWSER_CLOSE = True
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True

DATABASES = {'default': dj_database_url.config(
    default='postgres://{{ dbuser }}:{{ dbpassword }}@localhost:5432/{{ dbname }}'
)}

INSTALLED_APPS += (
    'djrill',
)

DEFAULT_FROM_EMAIL = 'info@webcampzg.org'
SERVER_EMAIL = 'info@webcampzg.org'

EMAIL_BACKEND = "djrill.mail.backends.djrill.DjrillBackend"
MANDRILL_API_KEY = "{{ mandrill_api_key }}"

