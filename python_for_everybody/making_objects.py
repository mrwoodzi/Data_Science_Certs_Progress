#Class - a template
#Attribute - a variable within a class
#Method - A function within a class
#Object - A Particular instance of a class
#Constructor - Code that runds when an object is created
#Inheritance - The ability to create a new class by extending an existing class


class PartyAnimal: 
    x = 0

    def __init__(self): # This is a "Constructor" which makes a new object
        print('I am constructed')

    def party(self):
        self.x = self.x + 1
        print('So far', self.x)

    def __del__(self):   # is seldom used, deletes value, deletes an and adds an = 42
        print('I am destructed', self.x)

an = PartyAnimal()
an.party()
an.party()
an = 42
print('an contains', an)
        