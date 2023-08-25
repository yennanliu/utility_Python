"""

# https://github.com/jvroig/AWS-Experiments-Lambda-Multithreading/blob/main/Lambdas/mp_noQueue/mp_noQueue.py
# https://docs.python.org/3/library/multiprocessing.html
# https://ithelp.ithome.com.tw/articles/10242047#:~:text=%E7%B7%9A%E7%A8%8B%E5%8F%AF%E4%BB%A5%E6%83%B3%E5%83%8F%E6%88%90%E5%AD%98%E5%9C%A8,%E9%80%B2%E7%A8%8B%E6%AF%94%E5%96%BB%E7%82%BA%E4%B8%80%E5%80%8B%E5%B7%A5%E5%BB%A0%EF%BC%8C

# https://stackoverflow.com/questions/38322574/python-multiprocessing-sharing-of-global-values

"""

import multiprocessing
import json
import os

counter = multiprocessing.Manager().Value('i',  0)
lock = multiprocessing.Manager().Lock()

def smile_detection(thread_name):
    global count, lock

    for x in range(10):
        with lock:
            counter.value +=1
            print (f"Process id = {os.getpid()}, input = {input}, thread_name = {thread_name}, counter value = {counter.value}")


def lambda_handler(event, context):


    x = multiprocessing.Process(target=smile_detection, args=("Thread1",))
    y = multiprocessing.Process(target=smile_detection, args=("Thread2",))
    x.start()
    y.start()
    x.join()
    y.join()

    resp =  {
        'statusCode': 200,
        'body': json.dumps('OK')
    }
    return resp
