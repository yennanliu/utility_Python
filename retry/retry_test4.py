"""
https://medium.com/@geethanjali.eswaran/retry-decorator-in-python-7605af5f2fb2
https://stackoverflow.com/questions/62763575/python-retry-with-dynamic-parameters
https://docs.python.org/3/library/functools.html
"""

from functools import wraps
import time

# retry decorator
def retry(retry_count=3, retry_interval=2):
    def real_decorator(decor_method):
        @wraps(decor_method)
        def wrapper(*args, **kwargs):
            for count in range(retry_count):
                try:
                    return_values = decor_method(*args, **kwargs)
                    return return_values
                except Exception as error:
                    # On exception, retry till retry_frequency is exhausted
                    print("FATAL: retry: %s . Function execution failed for %s" % (count + 1, decor_method.__name__))
                    time.sleep(retry_interval)
                    # If the retries are exhausted, raise the exception
                    if count == retry_count - 1:
                        raise error
        return wrapper
    return real_decorator


#@retry(retry_interval=3)
class MyClient:
    
    def __init__(self, name, age):


        self.name = name
        self.age = age

        #print (10/0)

        # if 3 > 2:
        #     raise Exception('3 > 2 Exception')
        if self.getDiff() < 0:
            raise Exception('getDiff Exception')

        print ('class init')

    def show(self):
        print (f'name = {self.name}, age = {self.age}')

    def getDiff(self):
        return 0 - 100


if __name__ == '__main__':
    client = retry(10, 2)(MyClient)('kyo', 99)
    client.show()
