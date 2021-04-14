# https://blog.louie.lu/2017/08/01/%E4%BD%A0%E6%89%80%E4%B8%8D%E7%9F%A5%E9%81%93%E7%9A%84-python-%E6%A8%99%E6%BA%96%E5%87%BD%E5%BC%8F%E5%BA%AB%E7%94%A8%E6%B3%95-06-concurrent-futures/

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
