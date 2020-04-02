import functools

def add(a, b):
    print(a + b)

add = functools.partial(add, 1)
add(2)
# outout : 3