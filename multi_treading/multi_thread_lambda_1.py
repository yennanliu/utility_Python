# https://github.com/jvroig/AWS-Experiments-Lambda-Multithreading/blob/main/Lambdas/mp_noQueue/mp_noQueue.py

import json
import os
import string
import time
from multiprocessing import Process

CHUNK_SIZE = 100
NUM_WORKERS = 3


def work_func(input):

    print (f"input = {input}")
    #time.sleep(1)
    return input

def lambda_handler(event, context):

    cnt = 0
    workers = {}

    for i in range(CHUNK_SIZE):
        
        # if number of worker > number of concurrent tasks
        if cnt < NUM_WORKERS:
            workers[cnt] = Process(target=work_func, args=(str(i),))
            workers[cnt].start()
        
        # Join all workers (make main thread wait until all spawned workers have finished)
        else:
            for i in range(num_workers):
                workers[i].join()
            # when all tasks fininished, reset cnt and start another batch
            cnt = 0
            workers[cnt] = Process(target=work_func, args=(str(i),))
            workers[cnt].start()

        cnt += 1

    # ??
    for i in range(num_workers):
        workers[i].join()
    resp =  {
        'statusCode': 200,
        'body': json.dumps('OK')
    }
    return resp
