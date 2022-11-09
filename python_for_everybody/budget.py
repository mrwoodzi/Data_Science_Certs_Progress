class Category:
  def __init__(self, name): # magic method/dunder method
    self.name = name # instance attribute
    self.ledger = [] # instance variable
    self.d = {} # instance variable
    self.balance = 0 # instance variable

  def __str__(self): # Instance method
    returnStr = ""
    returnStr += self.name.center(30, '*') + '\n'
    for a, b in self.d.items():
      returnStr +=  "{:<23}".format(a[:23]) + str(b).rjust(7) + '\n'
    returnStr += 'Total: '.ljust(2) + str(self.balance).rjust(2)
    return returnStr
  
  def percentage(self):
    return percentage
    pass

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

def create_spend_chart(*args):
  # show percentage spent in each category . . . Food, Clothing, Entertaiment
  # percentage spent should be calculated only with withdrawals
  # left side of chart should be label 1-100 in 10s
  # bars on bar chart should be "o"
  # each bar is rounded down to the nearest 10
  # horizontal line should go go 2 spaces past final bar in bar chart
  # each category name should be written vertically
  spend_chart = percentage(args)
  return spend_chart


food = Category("Food") #category
entertainment = Category("Entertainment")
business = Category("Business")
auto = Category("Auto") #category
clothing = Category("Clothing") #category        
food.deposit(100, "deposit")
print(food.balance)
food.withdraw(100.10)
print(food.balance)
food.deposit(100, "deposit")
food.deposit(400, "deposit")
food.transfer(200, entertainment)
print(entertainment.name, entertainment.balance)
food.deposit(1000, "initial deposit") #price
food.withdraw(600, "groceries") #quantity
food.withdraw(15.89, "restaurant and more food for dessert") #quantity
print(food.get_balance())



print(clothing.name, clothing.balance)
clothing.withdraw(25.55)#quantity
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
print(create_spend_chart(food))