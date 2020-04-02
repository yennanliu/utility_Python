# http://puremonkey2010.blogspot.com/2017/03/python-python-functools.html

from functools import wraps  
def wrap3(func):  
    @wraps(func)  
    def call_it(*args, **kwargs):  
        """Wrap func: call_it2"""  
        print ("Before call")
        return func(*args, **kwargs)  
    return call_it  
  
@wrap3  
def hello3():  
    """ Test hello 3"""  
    print ("Hello World3")  
  
if __name__ == '__main__':  
    hello3()  
    print (hello3.__name__) 
    print (hello3.__doc__)