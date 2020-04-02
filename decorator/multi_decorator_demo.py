# @a
# @b
# @c
# def d():
#     pass
#
# d = a(b(c(d)))

def a_func(func):
    def my_func(*args, **kwargs):
        print ("function a")
        return func(*args, **kwargs)
    return my_func

def b_func(func):
    def my_func(*args, **kwargs):
        print ("function b")
        return func(*args, **kwargs)
    return my_func

@a_func
@b_func
def c_func():
    print ("function c") 

c_func()