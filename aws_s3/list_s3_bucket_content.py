# python3 
# https://stackoverflow.com/questions/30249069/listing-contents-of-a-bucket-with-boto3


import boto3
from boto3 import client
from boto3.session import Session
import os 

# -------------------------------------
# config 
region_name=os.environ['region_name']
aws_access_key_id=os.environ['aws_access_key_id']
aws_secret_access_key=os.environ['aws_secret_access_key']
bucket_name=os.environ['bucket_name']
# -------------------------------------



# -------------------------------------

# 1) via boto3 resource  (#low-level functional API)
s3 = boto3.resource('s3', region_name=region_name,
                    aws_access_key_id=aws_access_key_id,
                    aws_secret_access_key=aws_secret_access_key)

conn = client('s3')  # again assumes boto.cfg setup, assume AWS S3
for key in conn.list_objects(Bucket=bucket_name)['Contents']:
    print(key['Key'])


# -------------------------------------


# 2) via session 
session = Session(aws_access_key_id=aws_access_key_id,
                  aws_secret_access_key=aws_secret_access_key)
s3 = session.resource('s3')
your_bucket = s3.Bucket(bucket_name)

for s3_file in your_bucket.objects.all():
    print(s3_file.key)








