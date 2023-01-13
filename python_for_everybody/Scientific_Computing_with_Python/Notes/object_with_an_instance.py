

class PartyAnimal: # This is a "Constructor" which makes a new object
    x = 0
    name = ""
    def __init__(self, z): # you can add a parameter 'z' onto the constructor, adds the argument Sally an Jim to
        self.name = z
        print(self.name, 'constructed')

    def party(self):
        self.x = self.x + 1
        print(self.name, 'party count', self.x)


s = PartyAnimal('Sally')
j = PartyAnimal('Jim')

s.party()
j.party()
s.party()
