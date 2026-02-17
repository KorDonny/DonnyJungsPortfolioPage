from django.http import JsonResponse
from django.views.decorators.http import require_GET
from services.projects_store import get_projects_payload
from services.signed_assets import get_resume_signed_url

@require_GET
def resume_signed_url(request):
    return JsonResponse(get_resume_signed_url())

@require_GET
def projects(request):
    return JsonResponse(get_projects_payload())