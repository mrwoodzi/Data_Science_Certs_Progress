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
    self.repop = copy.copy(self.contents)

  def repopulate(self):
    self.contents = copy.copy(self.repop)

  def draw(self, number):
    list_drawn_balls = []
    if number >= len(self.contents):
      self.contents = self.repop
      return self.contents
    for a in range(number):
      ball_index = random.randrange(len(self.contents))
      get_balls = self.contents.pop(ball_index)
      list_drawn_balls.append(get_balls)
    return list_drawn_balls

  def __str__(self):
    return self.colors

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  counts = 0
  experiment_count = 0
  for i in range(num_experiments):
    hat.repopulate()
    d = {}
    random_choices_list = hat.draw(num_balls_drawn)
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
    if len(new_key) == 0:
      continue
    elif len(new_key) == 1:
      continue
    elif len(new_key) == 2:
        if new_key[0] in expected_key and new_key[-1] in expected_key:
          if new_value[0] >= expected_value[0] and new_value[-1] >= expected_value[-1]:
            counts += 1
    elif len(new_key) == 3:
      if new_key[0] in expected_key and new_key[1] in expected_key and new_key[-1] in expected_key:
        if new_value[0] >= expected_value[0] and new_value[1] >= expected_value[1] and new_value[-1] >= expected_value[-1]:
          counts += 1

  probability = counts/num_experiments
  return probability


hat = Hat(blue=4, red=2, green=6)
experiment(hat=hat, expected_balls={"blue": 2,
                    "red": 1}, num_balls_drawn=4, num_experiments=100)
print("Probability:", experiment)

