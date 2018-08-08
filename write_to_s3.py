import boto3
import json
import datetime
import uuid
from pytz import timezone



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
