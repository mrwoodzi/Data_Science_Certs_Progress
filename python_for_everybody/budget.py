# needs a ledger that is a list


class Category:
  def __init__(self, name): # magic method, creates instance of person/instance object
    self.name = name
    self.ledger = []

  def deposit(self, amount=float, s=''):
    self.deposit = amount
    print(amount, s)
    

  def withdraw(self, amount=float, s=''):
    print(amount, s)
    self.withdraw = amount
  

  def get_balance(self):
    balance = (self.deposit) + (self.withdraw)
    return (f'${balance}')
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

food = Category("Food") #name
food.deposit(1000, "initial deposit") #price
food.withdraw(10.15, "groceries") #quantity
food.withdraw(15.89, "restaurant and more food for dessert") #quantity
#print(food.get_balance())

clothing = Category("Clothing") #name
food.transfer(50, "clothing") #quantity
clothing.withdraw(25.55)#quantity
clothing.withdraw(100)#quantity

auto = Category("Auto") #name
auto.deposit(1000, "initial deposit") #price
auto.withdraw(15)#quantity

print(str(food.get_balance))


