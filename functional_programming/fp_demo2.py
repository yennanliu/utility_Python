"""
FP VS OOP 
FP : split to data and pure function
OOP : Via class object, give object properties (dtype, value..), and methods under class 
"""

# fp 
wizard = {
  'name' : 'Merlin',
  'power' : 50   
}

def attack(char):
    return ('attack ! with power = {}'.format(char['power']))

print (attack(wizard))


# OOP 
class player:

    def __init__(self):
        self.name = 'Harry'
        self.power = 100

    def attack(self):
        return ('attack ! with power = {}'.format(self.power))

p = player()
print (p.attack())