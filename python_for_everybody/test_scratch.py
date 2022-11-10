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

   #def draw(self, number):
    #i = number
    #len_contents = len(self.contents)
    #deep_contents = copy.deepcopy(self.contents)
    #new_list = []
    #print(i)
    #print(len_contents)
    #print(self.contents)
    #while i > 0:
    #  contents = random.randrange(len(self.contents))
    #  newContents = self.contents.pop(contents)
    #  new_list.append(newContents)
    #  i -= 1
    #  len_contents -= 1
    #  if len_contents == 0 and i >= 1:
    #    self.contents = deep_contents
    #    len_contents = i
    #return new_list

  # Getting Percentage
total = 0
withdraw = 0
for d in args.d.values():
  print(d)
  if (float(d)) > 0:
    print("Total: ", d)
    total += (float(d))
  elif (float(d)) < 0:
    print("Withdraw: ", d)
    withdraw += abs(float((d)))
  percentage = round((withdraw/total), 2)
print(str(food))
print(total, withdraw)
print(percentage)

  def percentage(self):
    total = 0
    withdraw = 0
    for d in self.d.values():
      if (float(d)) > 0:
        print("Total: ", d)
        total += (float(d))
      elif (float(d)) < 0:
        print("Withdraw: ", d)
        withdraw += abs(float((d)))
    percentage = (round((withdraw/total), 2))
    return percentage
  
