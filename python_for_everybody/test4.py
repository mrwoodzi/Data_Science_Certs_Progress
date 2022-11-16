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
    ex_balls = []
    random_choices_list = random.choices(hat.contents, k=num_balls_drawn) # Had Sample here and thought the problem was with the draw method
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
      #print('len is 0', d, d_sorted, expected_balls)
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
          #print(new_value, expected_value)
          #print(new_key, expected_key)
          #print('this should add', counts, experiment_count, d, d_sorted, expected_balls)
    if experiment_count == 81:
      print(random_choices_list)
      print(new_value, expected_value)
      print(counts, experiment_count, d, d_sorted, expected_balls)
        
    
  probability = counts/num_experiments
  return probability