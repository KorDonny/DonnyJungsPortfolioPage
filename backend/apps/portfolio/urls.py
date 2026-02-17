from django.urls import path
from .views import get_resume_signed_url

urlpatterns = [
    path("assets/resume/", get_resume_signed_url, name="resume-signed-url"),
]
