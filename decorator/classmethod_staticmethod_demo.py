class PlayerCharacter:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def shout(self):
        print ("my name is {}".format(self.name))
        print ("my age is {}".format(self.age))

    def adding_things(self, num1, num2):
        print ("this is self adding_things")
        return ( num1 + num2 )


    @classmethod
    def adding_things_classmethod(cls, num1, num2): 
        """
        with the decorator @classmethod, the method can be used under class directly (PlayerCharacter.adding_things()),
        but no need to initiate first ( no need to run p = PlayerCharacter('judy', 10) first) 
        cls : class (PlayerCharacter in this case), means input class as one of the input
        """
        print ("this is classmethod")
        return ( num1 + num2 )

    @staticmethod
    def adding_thing_staticmethod(num1, num2): 
        """
        the only difference between classmethod, staticmethod is :
        in staticmethod, no need to input cls (class) variable.
        the use case is similar
        """
        print ("this is staticmethod")
        return ( num1 + num2 )


p = PlayerCharacter('judy', 10)
p.shout()
p.adding_things(10,20)
# classmethod demo
PlayerCharacter.adding_things_classmethod(9, 10)
# classmethod demo
PlayerCharacter.adding_thing_staticmethod(9, 10)
