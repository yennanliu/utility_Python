"""

# https://github.com/jvroig/AWS-Experiments-Lambda-Multithreading/blob/main/Lambdas/mp_noQueue/mp_noQueue.py
# https://docs.python.org/3/library/multiprocessing.html
# https://ithelp.ithome.com.tw/articles/10242047#:~:text=%E7%B7%9A%E7%A8%8B%E5%8F%AF%E4%BB%A5%E6%83%B3%E5%83%8F%E6%88%90%E5%AD%98%E5%9C%A8,%E9%80%B2%E7%A8%8B%E6%AF%94%E5%96%BB%E7%82%BA%E4%B8%80%E5%80%8B%E5%B7%A5%E5%BB%A0%EF%BC%8C

"""
import json
import os
import string
import time
from multiprocessing import Process

CHUNK_SIZE = 100
NUM_WORKERS = 3


def work_func(input):

    print (f"Process id = {os.getpid()}, input = {input}")
    #time.sleep(1)
    return input

def lambda_handler(event, context):

    cnt = 0
    workers = {}

    for i in range(CHUNK_SIZE):
        
        # if number of worker > number of parallel tasks
        if cnt < NUM_WORKERS:
            workers[cnt] = Process(target=work_func, args=(str(i),))
            workers[cnt].start()
        
        # Join all workers (make main thread wait until all spawned workers have finished)
        else:
            for i in range(NUM_WORKERS):
                workers[i].join()
            # when all tasks fininished, reset cnt and start another batch
            cnt = 0
            workers[cnt] = Process(target=work_func, args=(str(i),))
            workers[cnt].start()

        cnt += 1

    # ??
    for i in range(NUM_WORKERS):
        workers[i].join()
    resp =  {
        'statusCode': 200,
        'body': json.dumps('OK')
    }
    return resp
