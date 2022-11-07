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
    random_choices_list = random.sample(hat.contents, k=num_balls_drawn)
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
      print('len is 0', d, d_sorted, expected_balls)
      continue
    elif new_key[0] in expected_key and new_key[-1] in expected_key:
      if len(new_key) == 1:
        print('len is 1', d, d_sorted, expected_balls)
        continue
      elif new_value[0] >= expected_value[0] and new_value[-1] >= expected_value[-1]:
        counts += 1
        print(new_value[0], expected_value[0], new_value[-1], expected_value[-1])
        print(new_value, expected_value)
        print(new_key, expected_key)
        print('this should add', counts, d_sorted, expected_balls, experiment_count)
        

  probability = counts/num_experiments
  return probability


hat = Hat(yellow=5,red=1,green=3,blue=9,test=1)
experiment(hat=hat, expected_balls={"yellow":2,"blue":3,"test":1}, num_balls_drawn=19, num_experiments=100)
print("Probability:", experiment)

