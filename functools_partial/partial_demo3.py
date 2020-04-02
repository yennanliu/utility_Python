# http://puremonkey2010.blogspot.com/2017/03/python-python-functools.html

def wrap(func):  
    def call_it(*args, **kwargs):  
        """Wrap func: call_it """  
        print ("Before call") 
        return func(*args, **kwargs)  
    return call_it  
  
@wrap  
def hello():  
    """Say hello """  
    print ("Hello World")
  
from functools import update_wrapper  
def wrap2(func):  
    def call_it(*args, **kwargs):  
        """Wrap func: call_it2"""  
        print ("Before call")
        return func(*args, **kwargs)  
    return update_wrapper(call_it, func)  
  
@wrap2  
def hello2():  
    """ Test hello"""  
    print ("Hello World2")
  
if __name__ == '__main__':  
    hello()  
    print (hello.__name__)  
    print (hello.__doc__)  
    print ('-'*30)
    hello2() 
    print (hello2.__name__) 
    print (hello2.__doc__ )