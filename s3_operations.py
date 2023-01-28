import boto3
import os

# Retrieve the AWS credentials from environment variables
aws_access_key_id = os.environ['AWS_ACCESS_KEY_ID']
aws_secret_access_key = os.environ['AWS_SECRET_ACCESS_KEY']
region_name = os.environ['REGION']

current_path = os.path.dirname(os.path.abspath(__file__))

def list_buckets():
    s3 = boto3.client('s3', aws_access_key_id=aws_access_key_id,
                      aws_secret_access_key=aws_secret_access_key, region_name=region_name)
    response = s3.list_buckets()
    print(response['Buckets'])
    
def create_bucket(bucket_name):
    s3 = boto3.client('s3', aws_access_key_id=aws_access_key_id,
                      aws_secret_access_key=aws_secret_access_key, region_name=region_name)
    response = s3.create_bucket(Bucket=bucket_name)
    print(response)
    
def upload_to_s3(bucket_name, file_path):
    s3 = boto3.client('s3', aws_access_key_id=aws_access_key_id,
                      aws_secret_access_key=aws_secret_access_key, region_name=region_name)
    with open(file_path, 'rb') as f:
        s3.upload_fileobj(f, bucket_name, file_path)
    print(f"Successfully uploaded {file_path} to {bucket_name}")
    
def download_from_s3(bucket_name, key, local_path):
    s3 = boto3.client('s3', aws_access_key_id=aws_access_key_id,
                      aws_secret_access_key=aws_secret_access_key, region_name=region_name)
    s3.download_file(bucket_name, key, local_path)
    print(f"Successfully downloaded {key} from {bucket_name} to {local_path}")
    
def delete_from_s3(bucket_name, key):
    s3 = boto3.client('s3', aws_access_key_id=aws_access_key_id,
                      aws_secret_access_key=aws_secret_access_key, region_name=region_name)
    s3.delete_object(Bucket=bucket_name, Key=key)
    print(f"Successfully deleted {key} from {bucket_name}")
    
def delete_bucket(bucket_name):
    s3 = boto3.client('s3', aws_access_key_id=aws_access_key_id,
                      aws_secret_access_key=aws_secret_access_key, region_name=region_name)
    s3.delete_bucket(Bucket=bucket_name)
    print(f"Successfully deleted bucket {bucket_name}")


list_buckets()
create_bucket("sample-bucket-unique-name")
upload_to_s3("sample-bucket-unique-name", "file.txt")
download_from_s3("sample-bucket-unique-name", "file.txt", current_path)
delete_from_s3("sample-bucket-unique-name", "file.txt")
delete_bucket("sample-bucket-unique-name")

