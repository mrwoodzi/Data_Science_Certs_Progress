# needs a ledger that is a list


class Category:
  def __init__(self, budget_category): # magic method, creates instance of person/instance object
    category = str.lower(budget_category)
    print(category)
    if category == 'food':
      self.food = category
    elif category == 'clothing':
      self.clothing = category
    elif category == 'entertainment':
      self.entertainment = category

  def deposit(self, amount=float, s=''):
    print(amount, s)
  
  def withdraw(self, amount=float, s=''):
    print(amount, s)
  
  def get_balance(self):
    pass
    
  def transfer(self, amount=float, s=''):
    pass

  def check_funds(self, check_funds):
    pass
    
  def ledger(self):
    pass



def create_spend_chart(categories):
  pass

#def create_spend_chart():

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


