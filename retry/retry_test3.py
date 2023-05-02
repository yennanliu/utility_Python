"""
https://medium.com/@geethanjali.eswaran/retry-decorator-in-python-7605af5f2fb2
"""

import time

# retry decorator
# Example:
# @retry(3, 2) or @retry()
# def test():
#     pass
def retry(retry_count=3, retry_interval=2):
    """
    retry decorator
    """
    def real_decorator(decor_method):
        def wrapper(*args, **kwargs):
            for count in range(retry_count):
                try:
                    return_values = decor_method(*args, **kwargs)
                    return return_values
                except Exception as error:
                    # On exception, retry till retry_frequency is exhausted
                    print("FATAL: retry: %s . Function execution failed for %s" %
                                 (count + 1, decor_method.__name__))
                    # sleep for retry_interval
                    time.sleep(retry_interval)
                    # If the retries are exhausted, raise the exception
                    if count == retry_count-1:
                        raise error
        return wrapper
    return real_decorator


@retry(retry_count=10, retry_interval=3)
class MyClient:
    
    def __init__(self, name, age):

        self.name = name
        self.age = age
        print (10/0)
        print ('class init')

    def show(self):
        print (f'name = {self.name}, age = {self.age}')


if __name__ == '__main__':
    client = MyClient('kyo', 99)
    client.show()
