# python3

import os 
import boto3
from boto3 import client

# -------------------------------------
# config 
region_name=os.environ['region_name']
aws_access_key_id=os.environ['aws_access_key_id']
aws_secret_access_key=os.environ['aws_secret_access_key']
#bucket_name=os.environ['bucket_name']

# -------------------------------------

def get_connect_to_s3():
	s3 = boto3.resource('s3', region_name=region_name,
						aws_access_key_id=aws_access_key_id,
						aws_secret_access_key=aws_secret_access_key)
	client = boto3.client('s3') 
	return s3, client 