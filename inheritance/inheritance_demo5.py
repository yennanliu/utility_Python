class BaseFunc:
    def __init__(self):
        self.a = 100
        self.b = 10
        self.c = 0

    def plus(self, x, y):
        print (x + y)

    def minus(self, x, y):
        print (x - y)

class WorkFunc_a(BaseFunc):
    def __init__(self):
        pass

# test
my_work_func_a = WorkFunc_a()
my_work_func_a.plus(1, 2)
my_work_func_a.plus(3, 4)