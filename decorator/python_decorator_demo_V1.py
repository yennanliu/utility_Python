# http://www.cnblogs.com/rhcad/archive/2011/12/21/2295507.html
# http://www.cnblogs.com/huxi/archive/2011/03/01/1967600.html

# DEMO 1 
print (' -------------------  DEMO 1  -------------------')
def deco(func):
    print("before myfunc() called.")
    func()
    print("after myfunc() called.")
    return func

# Same as deco(myfunc())
@deco
def myfunc():
    print(" myfunc() called.")
#>>before myfunc() called.
#>>myfunc() called.
#>>after myfunc() called.

# DEMO 2 
print (' -------------------  DEMO 2  -------------------')
def deco(func):
    def _deco(a, b):
        print("before myfunc() called.")
        ret = func(a, b)
        print("  after myfunc() called. result: %s" % ret)
        return ret
    return _deco 
    #return f()
 
@deco
def myfunc(a, b):
    print(" myfunc(%s,%s) called." % (a, b))
    return a + b

myfunc(1, 2)

# as same as 
# deco(myfunc(1, 2))
#>>myfunc(1, 2)
#>>before myfunc() called.
#>> myfunc(1,2) called.
#>>  after myfunc() called. result: 3
#>>3

# DEMO 3 
print (' -------------------  DEMO 3  -------------------')
def deco(func):
    def _deco(*args, **kwargs):
        print("before %s called." % func.__name__)
        ret = func(*args, **kwargs)
        print("  after %s called. result: %s" % (func.__name__, ret))
        return ret
    return _deco
 
@deco
def myfunc(a, b):
    print(" myfunc(%s,%s) called." % (a, b))
    return a+b
 
@deco
def myfunc2(a, b, c):
    print(" myfunc2(%s,%s,%s) called." % (a, b, c))
    return a+b+c
    
myfunc(1, 2)  # deco(myfunc(1,2))
myfunc(3, 4) # deco(myfunc(3,4))
myfunc2(1, 2, 3) # deco(myfunc2(1,2,3))
myfunc2(3, 4, 5) # deco(myfunc2(3,4,5))

# DEMO 4 
print (' -------------------  DEMO 4  -------------------')
def deco(arg):
    def _deco(func):
        def __deco():
            print("before %s called [%s]." % (func.__name__, arg))
            func()
            print("  after %s called [%s]." % (func.__name__, arg))
        return __deco
    return _deco
 
@deco("mymodule")
def myfunc():
    print(" myfunc() called.")
 
@deco("module2")
def myfunc2():
    print(" myfunc2() called.")
 
myfunc()
myfunc2()

# DEMO 5 
print (' -------------------  DEMO 5 -------------------')
def deco(func):
    def _deco(*args, **kwargs):
        print ('before call func' )
        ret = func(*args, **kwargs)
        print ('after call func' )
        return ret
    return _deco

@deco
def myfunc(x,y):
    print ('x :', x )
    print ('y :', y )
    return (' x+y = ', x+y)

# DEMO 6
print (' -------------------  DEMO 6 -------------------')
import time 
def timeit(func):
    def wrapper():
        start = time.clock()
        func()
        end =time.clock()
        print  ('used:', end - start)
    return wrapper
 
@timeit
def foo():
    print ('in foo()')
 
foo()

# DEMO 7
print (' -------------------  DEMO 7 -------------------')
def my_deco(func):
    def _my_deco(*args, **kwargs):
        print ('check before run func() ... ')
        if func(*args, **kwargs) < 5:
            print ('to small.. ')
        else:
            print (' value OK .. ')
        print ('after checking func() ...')
    return _my_deco
      
@my_deco
def my_func(x,y):
    print ('x+y =' , x+y)
    return x+y

my_func(1,2)

# DEMO 8  
print (' -------------------  DEMO 8 -------------------')
def login(func):
    def _login(*args, **kwargs):
        if func(*args, **kwargs) == 'password':
            print (' login success !')
        else:
            print (' login failed !')
    return _login
        
# login(myaccount(password))    
@login
def myaccount(password):
    print (' proceed login ....')
    return password
    
myaccount('test')
myaccount('password')
