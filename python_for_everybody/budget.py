# needs a ledger that is a list


class Category:
  def __init__(self, name): # magic method, creates instance of person/instance object
    self.name = name # instance variable
    self.ledger = [] # ledger instance variable, also know as data attributes, c++ calls it data members

  def deposit(self, amount=float, s=''): # instance attribute
    pass
  
  def withdraw(self, amount=float, s=''): # instance attribute
    pass
  
  def get_balance(self): # instance attribute
    pass
    
  def transfer(self, amount=float, s=''): # instance attribute
    pass

  def check_funds(self, check_funds): # instance attribute
    pass
    
  def ledger(self):
    return self.name

  def __str__(self):
    self_name_str = str(self.name)
    return self_name_str


def create_spend_chart(categories):
  pass

food = Category("Food") #category
food.deposit(1000, "initial deposit") #price
food.withdraw(10.15, "groceries") #quantity
food.withdraw(15.89, "restaurant and more food for dessert") #quantity
#print(food.get_balance())

clothing = Category("Clothing") #category
food.transfer(50, "clothing") #quantity
clothing.withdraw(25.55)#quantity
clothing.withdraw(100)#quantity

auto = Category("Auto") #category
auto.deposit(1000, "initial deposit") #price
auto.withdraw(15)#quantity

#print(food.repr)
#print(str(food.get_balance))


