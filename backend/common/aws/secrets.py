# backend/common/aws/secrets.py
import json
import os
import time
from typing import Any, Dict, Optional

import boto3

_cached_secret: Optional[Dict[str, Any]] = None
_cached_at: float = 0.0

DEFAULT_TTL_SECONDS = int(os.getenv("SECRETS_CACHE_TTL", "300"))  # 5분 기본


def _fetch_secret_json_from_secrets_manager() -> Dict[str, Any]:
    """
    AWS Secrets Manager에서 SecretString(JSON)을 읽어 dict로 반환.
    환경변수:
      - CLOUDFRONT_SECRET_ID: Secrets Manager secret name or ARN
    """
    secret_id = os.environ["CLOUDFRONT_SECRET_ID"]

    client = boto3.client("secretsmanager", region_name=os.environ["AWS_REGION"])
    resp = client.get_secret_value(SecretId=secret_id)

    # 대부분 SecretString 사용
    secret_str = resp.get("SecretString")
    if not secret_str:
        # SecretBinary로 저장한 경우(드묾)
        secret_bin = resp.get("SecretBinary")
        if not secret_bin:
            raise RuntimeError("SecretString/SecretBinary not found in secret value")
        secret_str = secret_bin.decode("utf-8")

    return json.loads(secret_str)


def get_secret_json(force_refresh: bool = False, ttl_seconds: int = DEFAULT_TTL_SECONDS) -> Dict[str, Any]:
    """
    Secrets Manager 호출을 TTL 동안 캐싱해서 비용/지연을 줄임.
    - force_refresh=True면 즉시 다시 가져옴
    - ttl_seconds=0이면 매번 새로 가져옴
    """
    global _cached_secret, _cached_at

    now = time.time()
    is_valid = (_cached_secret is not None) and (ttl_seconds > 0) and ((now - _cached_at) < ttl_seconds)

    if force_refresh or not is_valid:
        # fetch 실패 시, 기존 캐시가 있으면 그걸로 버팀(가용성 우선)
        try:
            new_secret = _fetch_secret_json_from_secrets_manager()
        except Exception:
            if _cached_secret is not None:
                return _cached_secret
            raise

        _cached_secret = new_secret
        _cached_at = now

    assert _cached_secret is not None
    return _cached_secret
