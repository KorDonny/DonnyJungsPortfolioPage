# backend/app/config/settings/__init__.py
import os

env = os.environ.get("DJANGO_ENV", "local").lower()

if env == "prod":
    from .prod import *
else:
    from .local import *
