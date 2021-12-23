import boto3
import botocore

BUCKET_NAME = "coderbytechallengesandbox"


def is_matched(filename: str) -> bool:
    return filename.startswith("__cb__")


s3 = boto3.client('s3', config=botocore.client.Config(
    signature_version=botocore.UNSIGNED))
response = s3.list_objects(Bucket=BUCKET_NAME)

for content in response['Contents']:
    filename = content['Key']
    if is_matched(filename):
        print(filename)
