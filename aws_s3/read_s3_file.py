# python3 
# https://dluo.me/s3databoto3

import os 
import pandas as pd
import boto3
from boto3 import client


# -------------------------------------
# config 
region_name=os.environ['region_name']
aws_access_key_id=os.environ['aws_access_key_id']
aws_secret_access_key=os.environ['aws_secret_access_key']
bucket_name=os.environ['bucket_name']

s3_csv_path = os.environ['s3_csv_path']
# -------------------------------------




client = boto3.client('s3') 
obj = client.get_object(Bucket=bucket_name, Key=s3_csv_path)
grid_sizes = pd.read_csv(obj['Body']) # pandas df from csv 
print (' S3 csv file overview : ', grid_sizes.head())
 







