import copy
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
  counts = 0
  experiment_count = 0
  for i in range(num_experiments):
    d = {}
    random_choices_list = random.choices(hat.contents, k=num_balls_drawn)
    for item in random_choices_list: # we populate the dictionary with the random_choices_list
      if item in d:
        d[item] += 1
      else:
        d[item] = 1
    expected_key = list(expected_balls.keys())
    d_sorted = dict()
    for key in expected_key: # this filters and reorders d
      if len(d) == 1:
        continue
      elif key in d:
        d_sorted[key] = d[key]
      else:
        continue
    new_key = list(d_sorted.keys())
    new_value = list(d_sorted.values())
    expected_value = list(expected_balls.values())
    experiment_count += 1
    for item in expected_key:
      if item in new_key:
        counts += 1
      elif item not in new_key:
        counts -= 1
        

  probability = counts/num_experiments
  return probability


hat = Hat(yellow=5,red=1,green=3,blue=9,test=1)
experiment(hat=hat, expected_balls={"yellow":2,"blue":3,"test":1}, num_balls_drawn=20, num_experiments=100)
print("Probability:", experiment)

