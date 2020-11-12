class BaseFunc:
    def __init__(self):
        self.a = 100
        self.b = 10
        self.c = 0

    def plus(self, x, y):
        print (x + y)

    def minus(self, x, y):
        print (x - y)

class BaseFunc2:
    def get_type(self, x):
        print (type(x))

    def to_str(self, x):
        print ("the value in str : " + str(x))

# can inherit multiple classes, and use their methods
class WorkFunc_b(BaseFunc, BaseFunc2):
    def __init__(self):
        pass

# test
my_work_func_b = WorkFunc_b()
my_work_func_b.plus(1, 2)
my_work_func_b.plus(3, 4)
my_work_func_b.get_type([1,2,3])
my_work_func_b.to_str(42523452)