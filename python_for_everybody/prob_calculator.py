import copy
import random
# Consider using the modules imported above.

class Hat:
  def __init__(self, **kwargs):
    self.colors = kwargs # instance attrbute
    self.contents = [] # instance variable
    for c, n  in self.colors.items():
      n = n - 1
      while n >= 0:
        self.contents.append(c)
        n -= 1

 # The Hat class should have a draw method that accepts an argument indicating the number 
    # of balls to draw from the hat. This method should remove balls at random from contents 
    # and return those balls as a list of strings. The balls should not go back into the hat 
    # during the draw, similar to an urn experiment without replacement. If the number of balls 
    # to draw exceeds the available quantity, return all the balls.
  def draw(self, number):
    pass

  def __str__(self):
    return self.colors


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  pass

