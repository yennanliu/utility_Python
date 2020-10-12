from multiprocessing import Pool
import time

class MyClass2:
    def __init__(self):
        self.id = 123
        self.value = 100
        self.index = 30

    def get_value(self):
        return self.value

    def get_multiplyer(self):
        return self.index

    def plus_100(self, x):
        time.sleep(5)
        return ( self.get_value() + x + 100 ) * self.get_multiplyer()

if __name__ == '__main__':
    # run below command in CLI check the running python thread
    # ps -ef | grep 
    p = Pool(16)
    my_class = MyClass2()
    print(p.map(my_class.plus_100, [ i for i in range(100000) ]))