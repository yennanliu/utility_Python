"""

# https://github.com/jvroig/AWS-Experiments-Lambda-Multithreading/blob/main/Lambdas/mp_noQueue/mp_noQueue.py
# https://docs.python.org/3/library/multiprocessing.html
# https://ithelp.ithome.com.tw/articles/10242047#:~:text=%E7%B7%9A%E7%A8%8B%E5%8F%AF%E4%BB%A5%E6%83%B3%E5%83%8F%E6%88%90%E5%AD%98%E5%9C%A8,%E9%80%B2%E7%A8%8B%E6%AF%94%E5%96%BB%E7%82%BA%E4%B8%80%E5%80%8B%E5%B7%A5%E5%BB%A0%EF%BC%8C

# https://stackoverflow.com/questions/38322574/python-multiprocessing-sharing-of-global-values

"""

#import multiprocessing
import json
import os
import boto3
import datetime as dt
import concurrent.futures

# counter = multiprocessing.Manager().Value('i',  0)
# lock = multiprocessing.Manager().Lock()

BUCKET_NAME = "multiprocess-test"


def cur_time_formatter(format):

    return dt.datetime.utcnow().strftime(format)


def write_to_s3(s3_client, bucket_name, key_name, json_data):

    print(f"s3_client = {s3_client}, bucket_name = {bucket_name}, key_name = {key_name}, json_data = {json_data}")
    try:
        s3_client.put_object(Body=json.dumps(json_data), Bucket=bucket_name, Key=key_name)
    except Exception as e:
        print(f"s3 put object failed : {str(e)}")


def upload_to_s3(data_id):

    print (f"Process id = {os.getpid()}, input = {input}, data_id = {data_id}")

    # # global count, lock
    # _s3_client = boto3.client("s3")
    # #for chunk in range(100):
    #     # with lock:
    #     #     counter.value +=1
    # print (f"Process id = {os.getpid()}, input = {input}, thread_name = {thread_name}, counter value = {counter.value}")
    # cur_time, cur_date = cur_time_formatter('%Y-%m-%d-%H-%M-%S'), cur_time_formatter('%Y/%m/%d')
    # key_name = f"dev1/{cur_date}/{cur_time}-{data_id}.json"
    # resp_data = {"val": data_id}
    # print (f"resp_data = {resp_data}")
    # write_to_s3(_s3_client, BUCKET_NAME, key_name, resp_data)

def lambda_handler(event, context):

    _s3_client = boto3.client("s3")
    _list = [x for x in range(100)]

    # with concurrent.futures.ProcessPoolExecutor(max_workers=3) as executor:
    #     executor.map(upload_to_s3, _list)

    print(f"concurrent start")
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        executor.map(upload_to_s3, range(100))

    print(f"concurrent end")
    resp =  {
        'statusCode': 200,
        'body': json.dumps('OK')
    }
    return resp
