# needs a ledger that is a list

class Category:
  def __init__(self, name): # magic method, creates instance of person/instance object
    self.name = name # instance variable
    self.ledger = [] # ledger instance variable, also know as data attributes, c++ calls it data members, # creates a new empty list for each category
    self.balance = 0
    self.str = ''''''

  def deposit(self, amount=float, description=None): # instance attribute, also called class method? #dict.self{"amount": amount, "description": description}
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
    return self.ledger.append(to_ledger), self.to_balance(to_balance)

  #A withdraw method that is similar to the deposit method, but the amount passed in should be stored in the ledger as a negative number. If there are not enough funds, nothing should be added to the ledger. This method should return True if the withdrawal took place, and False otherwise
  def withdraw(self, amount=float, description=None): # instance attribute, also called class method?
    if amount > self.balance:
      return False
    else:
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
      to_ledger = (f'{cb_l}{amount_p}{dots} {amount_wstr}{comma} {description_p}{dots} {description_wstr}{cb_r}')
      to_balance = amount_wneg
      return True, self.ledger.append(to_ledger), self.to_balance(to_balance),
  
#A transfer method that accepts an amount and another budget category as arguments. The method should add a withdrawal with the amount and the description "Transfer to [Destination Budget Category]". The method should then add a deposit to the other budget category with the amount and the description "Transfer from [Source Budget Category]". If there are not enough funds, nothing should be added to either ledgers. This method should return True if the transfer took place, and False otherwise.
  def transfer(self, amount=float, description=None):# instance attribute, also called class method?
    print(amount, description)
    if amount > self.balance:
      return False
    else:
      amount_tneg = amount/-1
      amount_tstr = str(amount_tneg)
      #print((self))
      if description == '' or None:
        description_str == """''"""
      elif description != '' or None:
        description_tstr = f"'Transfer to {description}'"
      cb_l = '{'
      cb_r = '}'
      dots = ':'
      comma = ','
      amount_p = """'amount'"""
      description_p = """'description'"""
      to_ledger = (f'{cb_l}{amount_p}{dots} {amount_tstr}{comma} {description_p}{dots} {description_tstr}{cb_r}')
      to_balance = amount_tneg
      return True, self.ledger.append(to_ledger), self.to_balance(to_balance), description.to_balance(amount)
    
  def to_balance(self, to_balance):
    self.balance = to_balance + self.balance

  def to_ledger(self, to_ledger):
    self.ledger += to_ledger

  def to_string(self) -> str:
    return self.str
#A get_balance method that returns the current balance of the budget category based on the deposits and withdrawals that have occurred.
  def get_balance(self):
    return self.balance

#A check_funds method that accepts an amount as an argument. It returns False if the amount is greater than the balance of the budget category and returns True otherwise. This method should be used by both the withdraw method and transfer method.
  def check_funds(self, amount=None): # instance attribute, also called class method?
    check_funds = None
    if amount > self.balance:
      check_funds = False
      return check_funds
    elif amount < self.balance:
      check_funds = True
      return check_funds

  #A check_funds method that accepts an amount as an argument. It returns False if the amount is greater than the balance of the budget category and returns True otherwise. This method should be used by both the withdraw method and transfer method.
  def __str__(self) -> str:
      return self.name

def create_spend_chart(categories):
  pass


food = Category("Food") #category
entertainment = Category("Entertainment")
business = Category("Business")
auto = Category("Auto") #category
clothing = Category("Clothing") #category
food.deposit(100, "deposit")
food.deposit(400, "deposit")
food.transfer(200, entertainment)
food.deposit(1000, "initial deposit") #price
food.withdraw(600, "groceries") #quantity
food.withdraw(15.89, "restaurant and more food for dessert") #quantity
#print(food.get_balance())


food.transfer(50, "clothing") #quantity
clothing.withdraw(25.55)#quantity
clothing.withdraw(100)#quantity

auto.deposit(1000, "initial deposit") #price
auto.withdraw(15)#quantity

print(food)
print(clothing)
print(food.balance)
print(food.ledger[1])
#print((food.ledger))
#print((food.deposit))
#print(str(food.ledger[0]))
#print((clothing))
#print((auto))
#print((entertainment))
#print((business))