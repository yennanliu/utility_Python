# https://stackoverflow.com/questions/65812738/calling-a-python-decorator-with-args-directly-i-e-not-wrapping-another-functio

from functools import partial, wraps

def my_decorator_with_args(decorator_arg):
    def decorator(func):
        @wraps(func)
        def inner(*args, **kwargs):
            # some arbitrary logic using the decorator_arg(s)
            if decorator_arg == 100:
                print(f'Not running {func}')

            else:
                return func(*args, **kwargs)

        return inner

    return decorator


def add(x,y): 
    return x + y

p = partial(add, 1,2)

print('test 1')
z = my_decorator_with_args(100)(p)()
print (f'z = {z}')

print('')

print('test 2')
z = my_decorator_with_args(99)(p)()
print (f'z = {z}')
