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

  def draw(self, number):
    new_list = []
    for i in range(number):
      contents = random.randrange(len(self.contents))
      newContents = self.contents.pop(contents)
      new_list.append(newContents)
    return new_list

  def __str__(self):
    return self.colors

# For example, if you want to determine the probability of getting at least two red balls and one 
# green ball when you draw five balls from a hat containing six black, four red, and three green. 
# To do this, you will perform N experiments, count how many times M you get at least two red 
# balls and one green ball, and estimate the probability as M/N. Each experiment consists of 
# starting with a hat containing the specified balls, drawing several balls, and checking if 
# you got the balls you were attempting to draw.
def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  for i in range(num_experiments):
    d = {}
    counts = 0
    random_choices_list = random.sample(hat.contents, k=num_balls_drawn)
    for item in random_choices_list: # we populate the dictionary with the random_choices_list
      if item in d:
        d[item] += 1
      else:
        d[item] = 1
    print(expected_balls, d)
    for s, b in expected_balls.items(), d.items(): # iterating and comparing dict()
    print(counts)
  # compare d with expected_balls
  # if numbers match add to count
  # probability = counts/num_experiments
  # return probability

hat = Hat(blue=4, red=2, green=6)
probability = experiment(
    hat=hat,
    expected_balls={"blue": 2,
                    "red": 1},
    num_balls_drawn=4,
    num_experiments=4)
print("Probability:", probability)