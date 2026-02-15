FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

# deps
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# source
COPY app/ /app/

# App Runner가 PORT 환경변수로 포트 준다
CMD sh -c "gunicorn config.wsgi:application --bind 0.0.0.0:${PORT:-8000}"
