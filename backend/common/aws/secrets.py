# backend/common/aws/secrets.py
import json
import os
import time
from typing import Any, Dict, Optional

import boto3

_cached_secret: Optional[Dict[str, Any]] = None
_cached_at: float = 0.0

DEFAULT_TTL_SECONDS = int(os.getenv("SECRETS_CACHE_TTL", "300"))  # 5분 기본


def _truthy(v: Optional[str]) -> bool:
    return str(v or "").strip().lower() in {"1", "true", "yes", "y", "on"}


def _use_aws_secrets() -> bool:
    # 로컬에서는 기본적으로 AWS Secrets Manager를 사용하지 않음
    django_env = os.getenv("DJANGO_ENV", "local").lower()
    if django_env in {"local", "dev", "development"}:
        return _truthy(os.getenv("USE_AWS_SECRETS", "false"))
    # prod/staging에서는 기본적으로 사용
    return _truthy(os.getenv("USE_AWS_SECRETS", "true"))


def _fetch_secret_json_from_env_or_file() -> Dict[str, Any]:
    """
    로컬 개발용:
    우선순위
      1) CLOUDFRONT_SECRET_JSON (JSON 문자열)
      2) CLOUDFRONT_SECRET_FILE (JSON 파일 경로)
      3) 개별 env: CLOUDFRONT_DOMAIN / CLOUDFRONT_KEY_PAIR_ID / CLOUDFRONT_PRIVATE_KEY_PEM
    """
    # 1) JSON string
    raw = os.getenv("CLOUDFRONT_SECRET_JSON")
    if raw:
        try:
            return json.loads(raw)
        except json.JSONDecodeError as e:
            raise RuntimeError(f"CLOUDFRONT_SECRET_JSON is not valid JSON: {e}") from e

    # 2) JSON file path
    path = os.getenv("CLOUDFRONT_SECRET_FILE")
    if path:
        try:
            with open(path, "r", encoding="utf-8") as f:
                return json.load(f)
        except FileNotFoundError as e:
            raise RuntimeError(f"CLOUDFRONT_SECRET_FILE not found: {path}") from e

    # 3) individual envs
    domain = os.getenv("CLOUDFRONT_DOMAIN")
    kpid = os.getenv("CLOUDFRONT_KEY_PAIR_ID")
    pk = os.getenv("CLOUDFRONT_PRIVATE_KEY_PEM")

    missing = [k for k, v in {
        "CLOUDFRONT_DOMAIN": domain,
        "CLOUDFRONT_KEY_PAIR_ID": kpid,
        "CLOUDFRONT_PRIVATE_KEY_PEM": pk,
    }.items() if not v]

    if missing:
        raise RuntimeError(
            "Local secrets are missing. Provide one of:\n"
            "- CLOUDFRONT_SECRET_JSON\n"
            "- CLOUDFRONT_SECRET_FILE\n"
            f"- or env vars: {', '.join(missing)}"
        )

    return {
        "CLOUDFRONT_DOMAIN": domain,
        "CLOUDFRONT_KEY_PAIR_ID": kpid,
        "CLOUDFRONT_PRIVATE_KEY_PEM": pk,
    }


def _fetch_secret_json_from_secrets_manager() -> Dict[str, Any]:
    """
    AWS Secrets Manager에서 SecretString(JSON)을 읽어 dict로 반환.
    환경변수:
      - CLOUDFRONT_SECRET_ID: Secrets Manager secret name or ARN
      - AWS_REGION
    """
    secret_id = os.environ["CLOUDFRONT_SECRET_ID"]
    region = os.environ.get("AWS_REGION", "ap-northeast-2")

    client = boto3.client("secretsmanager", region_name=region)
    resp = client.get_secret_value(SecretId=secret_id)

    secret_str = resp.get("SecretString")
    if not secret_str:
        secret_bin = resp.get("SecretBinary")
        if not secret_bin:
            raise RuntimeError("SecretString/SecretBinary not found in secret value")
        secret_str = secret_bin.decode("utf-8")

    return json.loads(secret_str)


def get_secret_json(force_refresh: bool = False, ttl_seconds: int = DEFAULT_TTL_SECONDS) -> Dict[str, Any]:
    """
    secrets를 TTL 동안 캐싱.
    - local(default): env/file에서 읽음 (AWS 크레덴셜 필요 없음)
    - prod(default): Secrets Manager에서 읽음
    """
    global _cached_secret, _cached_at

    now = time.time()
    is_valid = (_cached_secret is not None) and (ttl_seconds > 0) and ((now - _cached_at) < ttl_seconds)

    if force_refresh or not is_valid:
        try:
            if _use_aws_secrets():
                new_secret = _fetch_secret_json_from_secrets_manager()
            else:
                new_secret = _fetch_secret_json_from_env_or_file()
        except Exception:
            if _cached_secret is not None:
                return _cached_secret
            raise

        _cached_secret = new_secret
        _cached_at = now

    assert _cached_secret is not None
    return _cached_secret
