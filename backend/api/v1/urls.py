from django.urls import path
from django.http import JsonResponse
from api.v1 import views

def health(request):
    return JsonResponse({"status": "ok"})

urlpatterns = [
    path("health", health),                 # ✅ App Runner health check용 (/health)
    path("assets/resume/", views.resume_signed_url),
    path("projects/", views.projects),
    path("assets/bg/",views.background_signed_url),
]