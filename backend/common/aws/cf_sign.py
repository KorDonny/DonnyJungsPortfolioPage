import datetime
from botocore.signers import CloudFrontSigner
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import padding, rsa
from cryptography.hazmat.backends import default_backend  # (구버전 호환용, 가능하면 제거)

def _rsa_signer(message: bytes, private_key_pem: str) -> bytes:
    key = serialization.load_pem_private_key(
        private_key_pem.encode("utf-8"),
        password=None,
        # cryptography 최신에선 backend 인자 없이도 동작합니다.
        backend=default_backend(),
    )

    # Pylance 타입 + 런타임 안전성 확보 (RSA 키가 아니면 명확히 실패)
    if not isinstance(key, rsa.RSAPrivateKey):
        raise TypeError(f"Expected RSA private key, got: {type(key).__name__}")

    return key.sign(
        message,
        padding.PKCS1v15(),
        hashes.SHA1(),
    )

def make_signed_url(
    cf_domain: str,
    key_pair_id: str,
    private_key_pem: str,
    object_path: str,
    expires_seconds: int = 300,
) -> str:
    url = f"https://{cf_domain}{object_path}"
    expire = datetime.datetime.utcnow() + datetime.timedelta(seconds=expires_seconds)
    signer = CloudFrontSigner(key_pair_id, lambda m: _rsa_signer(m, private_key_pem))
    return signer.generate_presigned_url(url, date_less_than=expire)
