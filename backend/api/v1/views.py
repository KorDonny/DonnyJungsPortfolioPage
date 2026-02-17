from django.http import JsonResponse
from django.views.decorators.http import require_GET
from services.signed_assets import get_resume_signed_url

@require_GET
def resume_signed_url(request):
    return JsonResponse(get_resume_signed_url())
