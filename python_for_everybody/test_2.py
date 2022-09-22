    self.food = food
    self.clothing = clothing
    self.entertainment = entertainment
    self.auto = auto

    def __setattr__(self, name, s):
    print(name)
    self.food = food
    self.clothing = clothing
    self.entertainment = entertainment
    self.auto = auto

  def party(self):
    self.name = self.name + 1
    print('So far', self.x)
#Possible way to get rid of ""
    VERSION = ["'pilot-2'", "'pilot-1'"]
VERSIONS_F = [item [1:-1] for item in VERSION]
print(VERSIONS_F)


