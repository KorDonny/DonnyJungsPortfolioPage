from django.urls import path, include
from django.http import JsonResponse

def health(request):
    return JsonResponse({"status": "ok"})

urlpatterns = [
    path("health", health),                 # ✅ App Runner health check용 (/health)
    path("v1/", include("api.v1.urls"))
]