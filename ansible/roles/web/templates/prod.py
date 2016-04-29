from .base import *
import dj_database_url

DEBUG = False

ALLOWED_HOSTS = ['2016.webcampzg.org', '128.199.33.243']

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTOCOL', 'https')
SESSION_EXPIRE_AT_BROWSER_CLOSE = True
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True

DATABASES = {'default': dj_database_url.config(
    default='postgres://{{ dbuser }}:{{ dbpassword }}@localhost:5432/{{ dbname }}'
)}

DEFAULT_FROM_EMAIL = 'info@webcampzg.org'
SERVER_EMAIL = 'info@webcampzg.org'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.sendgrid.net'
EMAIL_HOST_USER = '{{ sendgrid_username }}'
EMAIL_HOST_PASSWORD = "{{ sendgrid_password }}"
EMAIL_PORT = 587
EMAIL_USE_TLS = True

RAVEN_CONFIG = {
    "dsn": "{{ raven_dsn }}"
}

ENTRIO_API_KEY = "{{ entrio_api_key }}"
