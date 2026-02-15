# app/portfolio/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path("v1/projects/", views.projects),  # /api/v1/projects/ 로 맞추려면 아래 3) 참고
]
