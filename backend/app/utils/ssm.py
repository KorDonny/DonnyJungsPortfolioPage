import os
import boto3

REGION = os.environ.get("AWS_REGION", "ap-northeast-2")

ssm = boto3.client("ssm", region_name=REGION)

def get_param(name: str, decrypt: bool = False) -> str:
    resp = ssm.get_parameter(Name=name, WithDecryption=decrypt)
    return resp["Parameter"]["Value"]