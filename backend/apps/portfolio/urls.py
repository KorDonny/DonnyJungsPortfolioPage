from django.urls import path
from .views import get_resume_signed_url

urlpatterns = [
    path("api/v1/assets/resume", get_resume_signed_url),
]
