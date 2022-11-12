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
  
total = 0
withdraw = 0
  for d in .d.values():
    #print(d)
    if (float(d)) > 0:
      #print("Total: ", d)
      total += (float(d))
    elif (float(d)) < 0:
      #print("Withdraw: ", d)
      withdraw += abs(float((d)))
  percentage = math.trunc((withdraw/total*10))

food.deposit(100, "deposit")
#print(food.balance)
food.withdraw(100.10)
#print(food.balance)
food.deposit(100, "deposit")
food.deposit(400, "deposit")
food.transfer(200, entertainment)
clothing.deposit(2000, "deposit")
entertainment.deposit(8938, "entertainment")
business.deposit(684, "business")
# print(entertainment.name, entertainment.balance)
food.deposit(1000, "initial deposit") #price
food.withdraw(600, "groceries") #quantity
food.withdraw(15.89, "restaurant and more food for dessert") #quantity
# print(food.get_balance())
entertainment.withdraw(234, "stuff")
business.withdraw(598, "more stuff")



# print(clothing.name, clothing.balance)
clothing.withdraw(250.55)#quantity
clothing.withdraw(100)#quantity

auto.deposit(1000, "initial deposit") #price
auto.withdraw(15)#quantity
#auto.withdraw(35.60)

#print(food)
#print(clothing)
#print(food.name, food.balance)
#print(auto.name, auto.balance)
#print(entertainment.name, entertainment.balance)
#print(food.ledger)
#print(entertainment.tran_balance)
#print(food.tran_balance)
#print((food.ledger))
#print((food.deposit))
#print(str(food.ledger[0]))
#print((clothing))
#print((auto))
#print((entertainment))
#print((business))

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
          #print('this should add', counts, d_sorted, expected_balls, experiment_count)
    # if counts >= 80 and counts <= 81:
      # print(counts, d, d_sorted, expected_balls, experiment_count)