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


Below is for __str__:
    #f"*************Food*************\ndeposit                 900.00\nmilk, cereal, eggs, bac -45.67\nTransfer to Entertainme -20.00\nTotal: 834.33"
    line_num = 30
    len_self = len(self.name)
    name = str(self.name)
    #print(len_self)
    star_num = ((line_num - len_self)/2)
    stars = '*' * (int(star_num))
    line = f'{stars}{name}{stars}\n'
    space = """ """
    line = to_string