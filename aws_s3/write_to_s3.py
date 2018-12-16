import boto3
import json
import datetime
import uuid
from pytz import timezone
import os 

try:
  AWS_KEY_ID = os.environ['AWS_KEY_ID']
  AWS_SECRET_KEY = os.environ['AWS_SECRET_KEY']
  bucketname = os.environ['bucketname']
except:
  print ('No S3 credential loaded')



# ok to use 
def save_to_S3(region_name,finename,bucketname):
  # https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html?highlight=upload#S3.Client.upload_file
  s3 = boto3.resource('s3',
                      region_name = region_name,
                      aws_access_key_id=AWS_KEY_ID,
                      aws_secret_access_key=AWS_SECRET_KEY)
  bucket = s3.Bucket(bucketname)

  try:
    s3.meta.client.upload_file(finename, bucketname, finename)
    print ('upload to S3 OK')
  except Exception as e:
    print (e)
    print ('upload failed')



# dev 
def write_to_s3(log_data, folder_name, model_name,region_name,aws_access_key_id,aws_secret_access_key,bucket_name):
    try:
        s3 = boto3.resource('s3', region_name=region_name,
                            aws_access_key_id=aws_access_key_id,
                            aws_secret_access_key=aws_secret_access_key)
        data = {}
        #data['timestamp'] = str(get_time())
        data['model'] = model_name
        data['data'] = log_data
        json_out = json.dumps(data)
        file_name = folder_name + '/' + str(uuid.uuid4()) + '.json'
        s3.Object(bucket_name, file_name).put(Body=json_out)
    except Exception as x:
        print(x)