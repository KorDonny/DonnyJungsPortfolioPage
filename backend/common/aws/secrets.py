import json, boto3, os

def get_secret_json():
    secret_name = os.environ.get("CF_SIGNING_SECRET_NAME", "portfolio/cloudfront/signing")
    region = os.environ.get("AWS_REGION", "ap-northeast-2")
    client = boto3.client("secretsmanager", region_name=region)
    resp = client.get_secret_value(SecretId=secret_name)
    return json.loads(resp["SecretString"])
