# needs a ledger that is a list


class Category:
  
  def __init__(self, name): # magic method, creates instance of person/instance object
    self.name = name # instance variable
    self.ledger = [] # ledger instance variable, also know as data attributes, c++ calls it data members, # creates a new empty list for each category
    self.balance = 0
    
  def deposit(self, amount=float, description=None): # instance attribute, also called class method?
    #dict.self{"amount": amount, "description": description}
    if description == '' or None:
      description == """''"""
    elif description != '' or None:
      description = """'deposit'"""
    cb_l = '{'
    cb_r = '}'
    dots = ':'
    comma = ','
    amount_p = """'amount'"""
    description_p = """'description'"""
    to_ledger = f'{cb_l}{amount_p}{dots} {amount}{comma} {description_p}{dots} {description}{cb_r}'
    to_balance = amount
    return self.ledger.append(to_ledger), self.to_balance(to_balance)
  
  def withdraw(self, amount=float, description=None): # instance attribute, also called class method?
    amount = amount/-1
    if description == '' or None:
      description == """''"""
    elif description != '':
      description = """'withdraw'"""
    cb_l = '{'
    cb_r = '}'
    dots = ':'
    comma = ','
    amount_p = """'amount'"""
    description_p = """'description'"""
    to_ledger = f'{cb_l}{amount_p}{dots} {amount}{comma} {description_p}{dots} {description}{cb_r}'
    to_balance = amount
    return self.ledger.append(to_ledger), self.to_balance(to_balance)
  

  def transfer(self, amount=float, description=None):# instance attribute, also called class method?
    amount = amount/-1
    if description == '' or None:
      description == """''"""
    elif description != '' or None:
      description = f"Transfer to {description}'"
    cb_l = '{'
    cb_r = '}'
    dots = ':'
    comma = ','
    amount_p = """'amount'"""
    description_p = """'description'"""
    to_ledger = f'{cb_l}{amount_p}{dots} {amount}{comma} {description_p}{dots} {description}{cb_r}'
    to_balance = amount
    return self.ledger.append(to_ledger)
  def to_balance(self, to_balance):
    self.balance = to_balance + self.balance
    return self.balance
    
  def get_balance(self):
    return self.balance

  def check_funds(self, check_funds): # instance attribute, also called class method?
    pass
    

  def ledger(self, ledger):
    return self.ledger

  def __str__(self, name=None):
    #f"*************Food*************\ndeposit                 900.00\nmilk, cereal, eggs, bac -45.67\nTransfer to Entertainme -20.00\nTotal: 834.33"
    self_name_str = str(self.name)
    return self_name_str

  def __repr__(self):
    return f"Category({self.name}, {self.ledger}, {self.balance})"

def create_spend_chart(categories):
  pass




food = Category("Food") #category
food.deposit(1000, "initial deposit") #price
food.withdraw(10.15, "groceries") #quantity
food.withdraw(15.89, "restaurant and more food for dessert") #quantity
print(food.get_balance())

clothing = Category("Clothing") #category
food.transfer(50, "clothing") #quantity
clothing.withdraw(25.55)#quantity
clothing.withdraw(100)#quantity

auto = Category("Auto") #category
auto.deposit(1000, "initial deposit") #price
auto.withdraw(15)#quantity
entertainment = Category("Entertainment")
business = Category("Business")
food.transfer(200, entertainment)


print(repr(food))
print(repr(clothing))
print(repr(auto))
print(repr(entertainment))
print(repr(business))

print(create_spend_chart([food, clothing, auto]))


