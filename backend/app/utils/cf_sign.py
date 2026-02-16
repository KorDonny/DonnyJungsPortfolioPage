import datetime
from botocore.signers import CloudFrontSigner
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend

def _rsa_signer(message: bytes, private_key_pem: str) -> bytes:
    private_key = serialization.load_pem_private_key(
        private_key_pem.encode("utf-8"),
        password=None,
        backend=default_backend(),
    )
    return private_key.sign(message)

def make_signed_url(cf_domain: str, key_pair_id: str, private_key_pem: str, object_path: str, expires_seconds: int = 300) -> str:
    url = f"https://{cf_domain}{object_path}"
    expire = datetime.datetime.utcnow() + datetime.timedelta(seconds=expires_seconds)
    signer = CloudFrontSigner(key_pair_id, lambda m: _rsa_signer(m, private_key_pem))
    return signer.generate_presigned_url(url, date_less_than=expire)
