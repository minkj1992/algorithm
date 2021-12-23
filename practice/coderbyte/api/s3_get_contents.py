import boto3
import botocore


BUCKET_NAME = "coderbytechallengesandbox"


def print_file(body: botocore.response.StreamingBody) -> None:
    file_data = body.read()
    contents = file_data.decode('utf-8')
    print(contents)


def is_matched_file(filename: str) -> bool:
    prefix = "__cb__"
    return filename.startswith(prefix)


s3 = boto3.client('s3', config=botocore.client.Config(
    signature_version=botocore.UNSIGNED))
response = s3.list_objects(Bucket=BUCKET_NAME)

for content in response['Contents']:
    filename = content['Key']
    if is_matched_file(filename):
        file_obj = s3.get_object(Bucket=BUCKET_NAME, Key=filename)
        print_file(file_obj['Body'])
