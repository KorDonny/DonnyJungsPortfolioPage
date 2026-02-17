from .base import *

DEBUG = True
SECRET_KEY = "django-insecure-CHANGE_ME_LOCAL_ONLY"
ALLOWED_HOSTS = ["*"]

CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
]
