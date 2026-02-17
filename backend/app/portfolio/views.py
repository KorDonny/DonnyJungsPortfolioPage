# backend/app/views.py
from django.http import JsonResponse
from django.views.decorators.http import require_GET
from utils.secrets import get_secret_json
from utils.cf_sign import make_signed_url

@require_GET
def get_resume_signed_url(request):
    sec = get_secret_json()

    private_key_pem = sec["CLOUDFRONT_PRIVATE_KEY_PEM"]
    key_pair_id = sec["CLOUDFRONT_KEY_PAIR_ID"]
    cf_domain = sec["CLOUDFRONT_DOMAIN"]

    signed = make_signed_url(
        cf_domain=cf_domain,
        key_pair_id=key_pair_id,
        private_key_pem=private_key_pem,
        object_path="/content/resume.pdf",
        expires_seconds=300,
    )
    return JsonResponse({"url": signed, "expiresIn": 300})
