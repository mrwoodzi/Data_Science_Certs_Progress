# Thiis is a part of OOP
# Extends an existing class
# Inheritance is also called subclass

class PartyAnimal: # This is a "Constructor" which makes a new object
    x = 0
    name = ""
    def __init__(self, z): # you can add a parameter 'z' onto the constructor, adds the argument Sally an Jim to
        self.name = z
        print(self.name, 'constructed')

    def party(self):
        self.x = self.x + 1
        print(self.name, 'party count', self.x)

class FootballFan(PartyAnimal): # this adds in another method to party animal
    points = 0
    def touchdown(self):
        self.points = self.points + 7
        self.party()
        print(self.name, 'points', self.points)


s = PartyAnimal('Sally')
s.party()

j = PartyAnimal('Jim')
j.party()
j.touchdown()