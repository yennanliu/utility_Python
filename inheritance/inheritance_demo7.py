class BaseFunc:
    def __init__(self):
        self.a = 100
        self.b = 10
        self.c = 0

    def plus(self, x, y):
        print (x + y)

    def minus(self, x, y):
        print (x - y)

    def get_default_max(self):
        return max(self.a, self.b, self.c)

class WorkFunc_c(BaseFunc):
    def __init__(self):
        # use BaseFunc's __init__ method, so will get the self.a , self.b, self.c value
        super().__init__()

# test
my_work_func_c = WorkFunc_c()
print (my_work_func_c.a)
print (my_work_func_c.b)
print (my_work_func_c.get_default_max())