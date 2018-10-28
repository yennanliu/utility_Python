
# python3 
# http://www.cnblogs.com/rhcad/archive/2011/12/21/2295507.html
# http://www.cnblogs.com/huxi/archive/2011/03/01/1967600.html




print (' -------------------  DEMO 1  -------------------')
# DEMO 1 



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



print (' -------------------  DEMO 2  -------------------')
# DEMO 2 


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




print (' -------------------  DEMO 3  -------------------')
# DEMO 3 

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



print (' -------------------  DEMO 4  -------------------')
# DEMO 4 


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










print (' -------------------  DEMO 5 -------------------')
# DEMO 5 


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




print (' -------------------  DEMO 6 -------------------')
# DEMO 6




















