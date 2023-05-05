
def do_twice(func):
    def wrapper_do_twice(*args, **kwargs):
        print (f'(do_twice) name = {name}')
        func(*args, **kwargs)
        func(*args, **kwargs)
    return wrapper_do_twice


class MyClient:
    
    def __init__(self, name, age):

        self.name = name
        self.age = age
        print ('class init')

    def show(self):
        print (f'name = {self.name}, age = {self.age}')

    # https://blog.csdn.net/weixin_45523154/article/details/102992355
    @staticmethod
    def getDiff():
        return 0 - 100

    def call(self):
        diff = MyClient.getDiff() # use getDiff method directly
        print (f'diff = {diff}')

    @do_twice
    def print_(self):
        print (self.name)


@do_twice
def print_():
    print ('123')

if __name__ == '__main__':
    c = MyClient('tim', 17)
    c.call()
    #print_()