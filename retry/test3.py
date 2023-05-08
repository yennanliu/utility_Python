import functools

def do_twice(func):
    print(f'decorator code run')
    @functools.wraps(func)
    def wrapper_do_twice(*args, **kwargs):
        print (f"(do_twice) name = {name}")
        func(*args, **kwargs)
        func(*args, **kwargs)
    return wrapper_do_twice

class Myclient:

    def __init__(self):
        pass

    @do_twice
    def print_(self):
        print ("Myclient print_")


def run():
    print ("run")


if __name__ == '__main__':
    run()