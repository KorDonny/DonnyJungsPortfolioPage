import os
from .base import *

DEBUG = False
SECRET_KEY = os.environ[
    "DJANGO_SECRET_KEY"
    ]

ALLOWED_HOSTS = [
    "api.donnyjungsweb.dedyn.io",
    "donnyjungsweb.dedyn.io",
    ".awsapprunner.com"
    ]

CORS_ALLOWED_ORIGINS = [
    "https://www.donnyjungsweb.dedyn.io",
    ]

CORS_ALLOW_METHODS = [
    "GET", "OPTIONS"
    ]

CORS_ALLOW_HEADERS = [
    "content-type", "authorization"
    ]

SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")

USE_X_FORWARDED_HOST = True
