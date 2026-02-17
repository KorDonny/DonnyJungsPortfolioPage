from common.aws.secrets import get_secret_json
from common.aws.cf_sign import make_signed_url

RESUME_OBJECT_PATH = "/private/content/resume_en.pdf"
RESUME_EXPIRES_SECONDS = 300


def get_resume_signed_url() -> dict:
    sec = get_secret_json()

    signed = make_signed_url(
        cf_domain=sec["CLOUDFRONT_DOMAIN"],
        key_pair_id=sec["CLOUDFRONT_KEY_PAIR_ID"],
        private_key_pem=sec["CLOUDFRONT_PRIVATE_KEY_PEM"],
        object_path=RESUME_OBJECT_PATH,
        expires_seconds=RESUME_EXPIRES_SECONDS,
    )

    return {"url": signed, "expiresIn": RESUME_EXPIRES_SECONDS}
