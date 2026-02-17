from .base import *
from pathlib import Path
import os
from dotenv import load_dotenv


BASE_DIR = Path(__file__).resolve().parents[2]  # 보통 backend/를 가리키게 맞춤
load_dotenv(BASE_DIR / ".env.local")            # ✅ backend/.env.local 로드

DEBUG = True
SECRET_KEY = "django-insecure-CHANGE_ME_LOCAL_ONLY"
ALLOWED_HOSTS = ["*"]

CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
]
