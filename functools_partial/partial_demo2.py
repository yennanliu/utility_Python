def outer(func):
    @functools.wraps(func)
    def inner(*args, **kwargs):
        print(f"before...")
        func(*args, **kwargs)
        print("after...")
    return inner

@outer
def add(a, b):
    """
    add operation
    """
    print(a + b)

add(1,2)