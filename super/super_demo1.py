class User:
    def __init__(self, email):
        self.email = email

    def sign_in(self):
        print ("logged in")

class Wizard(User):
    def __init__(self, name, power, email):
        """
        1st way to use init from  original class's (User) method via this inheritance
        """
        User.__init__(self, email)
        self.name = name
        self.power = power

    def attack(self):
        print ("attack with power = {}".format(self.power))

class Knight(User):
    def __init__(self, name, power, email):
        """
        # Via the "Super" syntax, we have our 2nd way to use init from  original class's (User) method 
        """
        super().__init__(email)
        self.name = name
        self.power = power

    def attack(self):
        print ("attack with power = {}".format(self.power))

wizard1 = Wizard("jim", "100", "xxx@gmail.com")
print (wizard1.email)
knight1 = Knight("tom", "999", "yyy@gmail.com")
print (knight1.email)
