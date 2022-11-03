import copy
import random
from collections import OrderedDict

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
  for i in range(num_experiments):
    d = {}
    random_choices_list = random.sample(hat.contents, k=num_balls_drawn)
    for item in random_choices_list: # we populate the dictionary with the random_choices_list
      if item in d:
        d[item] += 1
      else:
        d[item] = 1
    print(d)
    print(len(d))
    expected_key = list(expected_balls.keys())
    print(expected_key)
    d_sorted = dict()
    for key in expected_key:
      if (len(d)) <= 2:
        d_sorted[key] = d[key]
      else:
        continue
    print(d_sorted)
    new_key = list(d_sorted.keys())
    new_value = list(d_sorted.values())
    expected_value = list(expected_balls.values())
    #print(new_key)
    #print(expected_key)
    if new_key[0] in expected_key and new_key[-1] in expected_key:
      if len(new_key) == 1:
        continue
      elif new_value[0] > expected_value[0] and new_value[-1] >= expected_value[1]:
        counts += 1
        print(new_value[0], expected_value[0], new_value[-1], expected_value[-1])
        print(counts, expected_balls, d)

    

      


        
    #common_value_key_pairs = dict(d.items() & expected_balls.items())
    #print(common_value_key_pairs)
    # the below if only gives exact match, I need key to match plus 
    #if common_value_key_pairs == expected_balls:
      # counts +=  1
      # print("Yes", counts, common_value_key_pairs, expected_balls)

        
  probability = counts/num_experiments  
  return probability

hat = Hat(blue=4, red=2, green=6)
experiment(hat=hat, expected_balls={"blue": 2,"red": 1}, num_balls_drawn=4, num_experiments=30)
print("Probability:", experiment)

