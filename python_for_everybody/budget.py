import math

class Category:
  def __init__(self, name): # magic method/dunder method
    self.name = name # instance attribute
    self.ledger = [] # instance variable
    self.d = {} # instance variable
    self.balance = 0 # instance variable
    self.wd = 0

  def __str__(self): # Instance method
    returnStr = ""
    returnStr += self.name.center(30, '*') + '\n'
    for a, b in self.d.items():
      returnStr +=  "{:<23}".format(a[:23]) + str(b).rjust(7) + '\n'
    returnStr += 'Total: '.ljust(2) + str(self.balance).rjust(2)
    return returnStr
  

  def deposit(self, amount, description=""): # Instance Attribute Outside of Init
    self.ledger.append({
      'amount': float(amount), 'description': description
    })
    self.d[description] = format(amount, '.2f')
    self.balance += float(amount)

  def withdraw(self, amount, description=""): # Instance Attribute Outside of Init
    if self.check_funds(amount):
      self.ledger.append({
      'amount': -float(amount), 'description': description
    })
      self.d[description] = format(-float(amount), '.2f')
      self.balance -= float(amount)
      self.wd += float(amount)
      return True
    else:
      return False

  def transfer(self, amount, otherCat): # Instance Attribute 
    if self.check_funds(amount):
      otherCat.deposit(amount, 'Transfer from ' + self.name)
      self.withdraw(amount, 'Transfer to ' + otherCat.name)
      return True
    else:
      return False

  def get_balance(self): # Instance Attribute Outside of Init
    return self.balance

  def check_funds(self, amount): # Instance Method
    if amount > self.balance:
      return False
    return  True

  # Can I make a def percentage to pass to spend_chart?


def create_spend_chart(args): # How do I put in multiple args since *args not working
  # Total withdraws in all Categories divided by total withdraw added up in all categories
  # left side of chart should be label 1-100 in 10s
  # lside += None
  # bars on bar chart should be "o"
  # bside += None
  # each bar is rounded down to the nearest 10 
  # horizontal line should go go 2 spaces past final bar in bar chart
  # hline_ += None
  # each category name should be written vertically
  # cat_name += None
  total = 0
  spend_chart = ""
  for a in args:
    total += int(a.wd)
  for arg in args:
    spend_chart += "Percentage spent by category: " + f"{arg.name} " + str(math.trunc((arg.wd)/(total)*10)*10) + "\n"
  
    
  return spend_chart
  pass


food = Category("Food") #category
entertainment = Category("Entertainment")
business = Category("Business")
auto = Category("Auto") #category
clothing = Category("Clothing") #category        
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
auto.withdraw(35.60)

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
print(create_spend_chart([food, clothing, business, entertainment]))
