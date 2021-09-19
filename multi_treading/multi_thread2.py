#!/usr/bin/python3

# https://blog.louie.lu/2017/08/01/%e4%bd%a0%e6%89%80%e4%b8%8d%e7%9f%a5%e9%81%93%e7%9a%84-python-%e6%a8%99%e6%ba%96%e5%87%bd%e5%bc%8f%e5%ba%ab%e7%94%a8%e6%b3%95-06-concurrent-futures/

import logging
import concurrent.futures
import argparse, subprocess, os, sys
import threading

PARALLELISM  = 2

SAMPLE_BASE_CMD = """bash test.sh"""

def run_SAMPLE_BASE_CMD(x):
    print('-'*10 + threading.current_thread().name + '-'*10  + "  x = " + str(x))

    REPARTITION_BASE_CMD2 = """bash aa.sh {}""".format(x)
    repartition_cmd = REPARTITION_BASE_CMD2
    print (repartition_cmd)
    cmd = subprocess.Popen(repartition_cmd, stdout=subprocess.PIPE, shell=True)
    (dist_cp_log, err) = cmd.communicate()
    exit_code = cmd.wait()

    # if success
    if (exit_code == 0):
        print ("OK!")
        print ("-"*30)

    # if failed
    else:
        print ("failed!")
        print ("-"*30)

if __name__ == "__main__":
  
    with concurrent.futures.ThreadPoolExecutor(max_workers=PARALLELISM) as executor:

        URLS = ['1', '2', '3']

        URLS = list(range(10))

        future_to_url = {executor.submit(run_SAMPLE_BASE_CMD, url): url for url in URLS}
        for future in concurrent.futures.as_completed(future_to_url):
            url = future_to_url[future]
            try:
                data = future.result()
            except Exception as exc:
                print('%r generated an exception: %s' % (url, exc))
            else:
                print('%r' % (url))
