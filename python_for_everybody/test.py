import random

class Hat:
  def __init__(self, **kwargs):
    self.colors = kwargs # instance attrbute
    self.contents = [] # instance variable
    for c, n  in self.colors.items():
      n = n - 1
      while n >= 0:
        self.contents.append(c)
        n -= 1

  def draw(self, number):
    new_list = []
    for i in range(number):
      contents = random.randrange(len(self.contents))
      newContents = self.contents.pop(contents)
      new_list.append(newContents)
    return new_list

  def __str__(self):
    return self.colors

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    d = {}
  for i in range(num_experiments):
    

hat = Hat(black=6, red=4, green=3)
experiment(hat=hat, expected_balls={"red":2,"green":1}, num_balls_drawn=5, num_experiments=20)