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
            #print (f'current_time = {current_time}')
            #print (f'to_catch_time = {to_catch_time}')
            count = 0
            while current_time < to_catch_time:
            #while current_time < to_catch_time or count < 5:
            #while True:
                try:
                    print (f'current_time = {current_time}')
                    print (f'to_catch_time = {to_catch_time}')
                    time.sleep(rerun_interval)
                    count += 1
                    current_time = datetime.datetime.now()
                    return_values = decor_method(*args, **kwargs)
                    #return return_values
                    print(f'Rerun : count = {count}, to_catch_time = {to_catch_time}, rerun_interval = {rerun_interval}')                    
                    print (f'return_values = {return_values}')
                except Exception as error:
                    print(f'Rerun : count = {count}, to_catch_time = {to_catch_time}, rerun_interval = {rerun_interval}, error = {error}')
        return _decorator
    return real_decorator


TO_CATCH = datetime.datetime.now() + datetime.timedelta(seconds=7)
RERUN_INTERVAl = 2

@rerun(to_catch_time=TO_CATCH, rerun_interval=RERUN_INTERVAl)
class MyClient:
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        #print (10/0)
        #time.sleep(1)
        print ('class init')

    def show(self):
        print (f'name = {self.name}, age = {self.age}')

    def getDiff(self):
        return 0 - 100


if __name__ == '__main__':
    client = MyClient('kyo', 99)
    #client.show()
