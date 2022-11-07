import random
import copy
contents_me = ["yellow", "yellow","yellow","yellow", "red", "yellow", "green", "green","green", "blue", "blue","blue","blue","blue","blue","blue","blue","blue",  "test"]
i = 20
new_list = []
len_contents = len(contents_me)
deep_copy = copy.deepcopy(contents_me)

while i > 0:

  print(i)
  print(len_contents)
  print(contents_me)
  contents = random.randrange(len(contents_me))
  newContents = contents_me.pop(contents)
  new_list.append(newContents)
  i -= 1
  len_contents -= 1
  if len_contents == 0 and i >= 1:
    contents_me = deep_copy
    len_contents == i
print(new_list)
  
