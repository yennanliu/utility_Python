"""
https://medium.com/@geethanjali.eswaran/retry-decorator-in-python-7605af5f2fb2
https://stackoverflow.com/questions/62763575/python-retry-with-dynamic-parameters
https://docs.python.org/3/library/functools.html
"""

from functools import wraps
import time, datetime

def rerun(to_catch_time, rerun_interval=1):
    def real_decorator(decor_method):
        def _decorator(*args, **kwargs):
            current_time = datetime.datetime.now()
            print (f'current_time = {current_time}')
            print (f'to_catch_time = {to_catch_time}')
            count = 0
            while current_time < to_catch_time:
            #while True:
                try:
                    print (f'current_time = {current_time}')
                    print (f'to_catch_time = {to_catch_time}')
                    current_time = datetime.datetime.now()
                    return_values = decor_method(*args, **kwargs)
                    #return return_values
                    print (f'return_values = {return_values}')
                except Exception as error:
                    # On exception, retry till retry_frequency is exhausted
                    #print("FATAL: rerun: %s . Function execution failed for %s.  retry interval = %s " %(count + 1, decor_method.__name__, retry_interval))
                    print(f'Rerun : count = {count}, to_catch_time = {to_catch_time}, rerun_interval = {rerun_interval}, error = {error}')
                    # sleep for rerun_interval
                    time.sleep(rerun_interval)
                    print(f'rerun exception : {Exception}')
        return _decorator
    return real_decorator


#@retry(retry_interval=3)
class MyClient:
    
    def __init__(self, name, age):

        self.name = name
        self.age = age
        #print (10/0)

        # if 3 > 2:
        #     raise Exception('3 > 2 Exception')
        # if self.getDiff() < 0:
        #     raise Exception('getDiff Exception')

        time.sleep(1)

        print ('class init')

    def show(self):
        print (f'name = {self.name}, age = {self.age}')

    def getDiff(self):
        return 0 - 100


if __name__ == '__main__':
    #timestamp = 1625309472.357246
    # convert to datetime
    #date_time = datetime.datetime.fromtimestamp(timestamp)
    to_catch_time = datetime.datetime.now() + datetime.timedelta(seconds=3)
    #print(f'date_time = {date_time}')
    client = rerun(to_catch_time, 5)(MyClient)('kyo', 99)
    #client.show()
