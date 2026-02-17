# backend/app/config/settings/prod.py
import os
from .base import *

DEBUG = False
SECRET_KEY = os.environ["DJANGO_SECRET_KEY"]

ALLOWED_HOSTS = [
    "api.donnyjungsweb.dedyn.io",
    "donnyjungsweb.dedyn.io",
]

CORS_ALLOWED_ORIGINS = [
    "https://www.donnyjungsweb.dedyn.io",
]
