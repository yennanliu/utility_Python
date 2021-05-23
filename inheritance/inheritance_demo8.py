# django Book for web application p.283

class BaseClass:

    def test(self):
        print ("BaseClass")

class Mix1:

    def ability1(self):
        print ("getability1")

    def test(self):
        print ("Mix1")

class Mix2:

    def ability2(self):
        print ("ability2")

    def test(self):
        print ("Mix2")


# inheritance
class TestClass1(Mix1):
    pass

class TestClass2(Mix2, Mix1, BaseClass):
    pass


# run
t1 = TestClass1()
t1.ability1()
t1.test()

print("="*30)

t2 = TestClass2()
t2.ability2()
t2.ability1()
t2.test()
