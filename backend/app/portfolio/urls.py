from django.urls import path
from .views import projects

urlpatterns = [
    path("v1/projects", projects),
]
