from multiprocessing import Pool

class MyClass:
    def __init__(self):
        self.id = 123
        self.value = 100

    def get_value(self):
        return self.value

    def plus_100(self, x):
        return x + 100

    def run_parallel(self):
        p = Pool(5)
        print(p.map(self.plus_100, [ i for i in range(100) ]))


if __name__ == '__main__':
    p = Pool(5)
    my_class = MyClass()
    my_class.run_parallel()