import copy
import random
import reprlib
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

  def draw(self, number):
    new_list = []
    for i in range(number):
      contents = random.randrange(len(self.contents))
      newContents = self.contents.pop(contents)
      new_list.append(newContents)
    return new_list

  def __str__(self):
    return self.colors

# For example, if you want to determine the probability of getting at least two red balls and one green ball when you draw five balls from a hat containing six black, four red, and three green. To do this, you will perform N experiments, count how many times M you get at least two red balls and one green ball, and estimate the probability as M/N. Each experiment consists of starting with a hat containing the specified balls, drawing several balls, and checking if you got the balls you were attempting to draw.
def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  print(hat, expected_balls, num_balls_drawn, num_experiments)
  # random_choices_list = 
  # count_choices = random_choices_list.count()
  # compare dict() with expected_balls
  # if numbers match add to count
  # run experiment again
    

  # return probability

hat = Hat(blue=4, red=2, green=6)
print(hat)
probability = experiment(
    hat=hat,
    expected_balls={"blue": 2,
                    "red": 1},
    num_balls_drawn=4,
    num_experiments=3000)
print("Probability:", probability)

