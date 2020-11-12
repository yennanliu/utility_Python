# https://www.w3schools.com/python/python_inheritance.asp

class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

# now, have a Student class inherit Person class and with __init__ method amd super()
class Student(Person):
    def __init__(self, fname, lname, year):
        # Python also has a super() function that will make the child class inherit all the methods and properties from its parent:
        # super means "use the original method that this class inherit from"
        super().__init__(fname, lname)
        self.my_year = year

# test the Student method
x = Student("mile", "oreal", 32)
x.printname()
print (x.firstname, x.lastname)
print (x.firstname, x.lastname, x.my_year)