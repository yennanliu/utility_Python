# parent class
class User():
    def sign_in(self):
        print ("logged in")

# children class
class Wizard(User):  ### inheritance via this method ###
    def __init__(self, name, power):
        self.name = name
        self.power = power 

    def attack(self):
        print ("attack with power = {}".format(self.power))

class Knight(User):   ### inheritance via this method ###
    def __init__(self, name, arrows):
        self.name = name
        self.arrows = arrows 

    def attack(self):
        print ("attack with arrows = {}".format(self.arrows))


Wizard1 = Wizard("Merlin", 50)
Knight1 = Knight("Bob", 100)

# -----------------
# polymorphism 
# -----------------

# via this player_attack func, 
# we can call the same method, 
# but have different op when input with different class
def player_attack(char):
    char.attack()

player_attack(Wizard1)
player_attack(Knight1)
