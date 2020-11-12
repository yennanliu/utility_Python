# https://www.w3schools.com/python/python_inheritance.asp

class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

# now, have a Student class inherit Person class and with __init__ method
class Student(Person):
	def __init__(self, fname, lname):
		Person.__init__(self, fname, lname)

# test the Student method
x = Student("mile", "oreal")
x.printname()
print (x.firstname, x.lastname)