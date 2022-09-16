class Category:
  def __init__(self, name): # magic method, creates instance of person/instance object
    self.name = name # instance variable
    self.ledger = """""" # ledger instance variable, also know as data attributes, c++ calls it data members, # creates a new empty list for each category
    self.balance = 0
    self.check_funds = False
    self.str = """ """

  def deposit(self, amount=float, description=None): # instance attribute, also called class method?
    #dict.self{"amount": amount, "description": description}
    amount_dstr = str(amount)
    description_dstr = str(description)
    if description_dstr == '' or None:
      description_dstr == """''"""
    elif description_dstr != '' or None:
      description_dstr = """'deposit'"""
    cb_l = '{'
    cb_r = '}'
    dots = ':'
    comma = ','
    amount_p = """'amount'"""
    description_p = """'description'"""
    to_ledger = f'{cb_l}{amount_p}{dots} {amount_dstr }{comma} {description_p}{dots} {description_dstr}{cb_r}'
    to_balance = amount
    return self.ledger(to_ledger), self.to_balance(to_balance)
  
  def withdraw(self, amount=float, description=None): # instance attribute, also called class method?
    amount_wneg = amount/-1
    amount_wstr = str(amount_wneg)
    description_wstr = str(description)
    if description_wstr == '' or None:
      description_wstr == """''"""
    elif description_wstr != '' or None:
      description_wstr = """'withdraw'"""
    cb_l = '{'
    cb_r = '}'
    dots = ':'
    comma = ','
    amount_p = """'amount'"""
    description_p = """'description'"""
    to_ledger = f'{cb_l}{amount_p}{dots} {amount_wstr}{comma} {description_p}{dots} {description_wstr}{cb_r}'
    to_balance = amount
    print(to_ledger)
    return self.ledger(to_ledger), self.to_balance(to_balance)
  

  def transfer(self, amount=float, description=None):# instance attribute, also called class method?
    amount_tneg = amount/-1
    amount_tstr = str(amount_tneg)
    #print(repr(self))
    description_tstr = str(description.name)
    if description == '' or None:
      description_str == """''"""
    elif description != '' or None:
      description_tstr = f"'Transfer to {description_tstr}'"
    cb_l = '{'
    cb_r = '}'
    dots = ':'
    comma = ','
    amount_p = """'amount'"""
    description_p = """'description'"""
    to_ledger = f'{cb_l}{amount_p}{dots} {amount_tstr}{comma} {description_p}{dots} {description_tstr}{cb_r}'
    to_balance = amount_tneg
    return self.ledger(to_ledger), self.to_balance(to_balance)
    
  def to_balance(self, to_balance):
    self.balance = to_balance + self.balance
    return self.balance
    
  def get_balance(self):
    return self.balance

  def check_funds(self, check_funds): # instance attribute, also called class method?
    if self.check_funds:
      self.check_funds = True
    return self.check_funds
    

  def ledger(self, to_ledger):
    self.ledger = self.ledger + to_ledger
    return self.ledger
    
    
  def __str__(self, to_ledger):
    #f"*************Food*************\ndeposit                 900.00\nmilk, cereal, eggs, bac -45.67\nTransfer to Entertainme -20.00\nTotal: 834.33"
    self.str = to_ledger + self.str
    line_num = 30
    len_self = len(self.name)
    name = self.name
    #print(len_self)
    star_num = ((line_num - len_self)/2)
    stars = '*' * (int(star_num))
    line = f'{stars}{name}{stars}\n'
    space = """ """
    #print(line)
    return line, self.str

  def __repr__(self):
    return f"Category({self.name}, {self.str}, {self.balance})"

def create_spend_chart(categories):
  pass


def create_spend_chart(categories):
  pass

food = Category("Food") #category
entertainment = Category("Entertainment")
business = Category("Business")
auto = Category("Auto") #category
clothing = Category("Clothing") #category
food.deposit(100, "deposit")
food.transfer(200, entertainment)
#food.deposit(1000, "initial deposit") #price
#food.withdraw(10.15, "groceries") #quantity
#food.withdraw(15.89, "restaurant and more food for dessert") #quantity
#print(food.get_balance())


#food.transfer(50, "clothing") #quantity
#clothing.withdraw(25.55)#quantity
#clothing.withdraw(100)#quantity

#auto.deposit(1000, "initial deposit") #price
#auto.withdraw(15)#quantity



print(repr(food.ledger))
print(repr(food.deposit))
print(str(food.ledger[0]))
#print(repr(clothing))
#print(repr(auto))
#print(repr(entertainment))
#print(repr(business))


def create_spend_chart(food, clothing, auto):
  pass