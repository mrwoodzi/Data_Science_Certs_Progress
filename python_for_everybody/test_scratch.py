class Category:
  def __init__(self, name): # magic method, creates instance of person/instance object
    self.name = name # instance variable
    self.ledger = [] # ledger instance variable, also know as data attributes, c++ calls it data members, # creates a new empty list for each category
    self.balance = 0
    self.str = ''''''
    self.dictionary = {'amount': None, "description": None}

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
    #self.ledger.append(to_ledger), 
    return self.to_balance(to_balance), self.to_dict(description, amount), self.ledger.append(to_ledger)
    
  def to_balance(self, to_balance):
    self.balance = to_balance + self.balance

  def to_ledger(self, to_ledger):
    to_ledger_s = str(to_ledger)
    self_ledger_s = str(self.ledger)
    self.ledger = to_ledger_s + self_ledger_s
    pass

  def to_string(self) -> str:
    for x in self.ledger:
      self.str = x
    return self.str

  def __str__(self) -> str:
    return self.name

  def to_dict(self, description, amount):
    self.dictionary["amount"] = amount
    self.dictionary["description"] = description
    print(self.dictionary)
    return self.dictionary




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
food.deposit(400, "deposit")
food.deposit(300, "deposit")
#food.transfer(200, entertainment)
#food.deposit(1000, "initial deposit") #price
#food.withdraw(10.15, "groceries") #quantity
#food.withdraw(15.89, "restaurant and more food for dessert") #quantity
#print(food.get_balance())


#food.transfer(50, "clothing") #quantity
#clothing.withdraw(25.55)#quantity
#clothing.withdraw(100)#quantity

#auto.deposit(1000, "initial deposit") #price
#auto.withdraw(15)#quantity

print(food)
print(clothing)
print(food.balance)
print(food.ledger[0])
print(food.dictionary)
#print(repr(food.ledger))
#print(repr(food.deposit))
#print(str(food.ledger[0]))
#print(repr(clothing))
#print(repr(auto))
#print(repr(entertainment))
#print(repr(business))


