class Category:
  # something = something # class attributes would go up here that would apply to all instance objects
  def __init__(self, name): # magic method, creates instance of person/instance object
    self.name = name # instance variable
    self.ledger = [] # ledger instance variable, also know as attributes or data attributes, c++ calls it data members, # creates a new empty list for each category

  def deposit(self, amount=float, description=''): # instance attribute, also called class method?
    #dict.self{"amount": amount, "description": description}
    if description == '':
      description == description
    elif description != '':
      description = 'deposit'
    self.add_ledger = f'"amount": {amount}, "description": "{description}"'
    to_ledger = (str(amount)) + description
    return self.ledger.append(to_ledger)
    return to_ledger

  
  def withdraw(self, amount=float, description=''): # instance attribute, also called class method?
    amount = (str(amount/-1))
    to_ledger = (str(amount)) + description
    return self.ledger.append(to_ledger)

  
  def get_balance(self): # instance attribute, also called class method?
    pass
    
  def transfer(self, amount=float, description=''): # instance attribute, also called class method?
    to_ledger = (str(amount)) + description
    return self.ledger.append(to_ledger)


  def check_funds(self, check_funds): # instance attribute, also called class method?
    pass 

  def ledger(self):
      return self.ledger

  def __str__(self):
    self_name_str = str(self.name)
    return self_name_str

  def __repr__(self):
    return f"Category({self.name}, {self.ledger})"


def create_spend_chart(categories):
  pass
