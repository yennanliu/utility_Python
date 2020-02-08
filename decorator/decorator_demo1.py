# 1) Decorator demo 
def my_decorator(func):
    def wrap_func():
        print ("********")
        func()
        print ("********")
    return wrap_func

# decotate hello with my_decorator
@my_decorator
def hello():
    print ("helooooooooooo") 

# decotate bye with my_decorator
@my_decorator
def bye():
    print ("see ya later") 

hello()
bye()


# 2) Decorator : put to-be-decorated-func as input into decorator func
"""
above decorator operations are literally as same as below:
i.e. :
     a) decorator_func(func) 

     is as same as 

     b) @decorator_func
         def func()
     
"""
def hello():
    print ("helooooooooooo") 

hello2 = my_decorator(hello)
hello2()

def bye():
    print ("see ya later") 

bye2 = my_decorator(bye)
bye2()
