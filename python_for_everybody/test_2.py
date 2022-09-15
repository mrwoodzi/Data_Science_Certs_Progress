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