# needs a ledger that is a list

class Category:
  def __init__(self, name): # magic method, creates instance of person/instance object
    self.name = name # instance variable
    self.ledger = [] # ledger instance variable, also know as data attributes, c++ calls it data members, # creates a new empty list for each category
    self.balance = 0

  def __str__(self):
    returnStr = ""
    returnStr += self.name.center(30, '*') + '\n'
    returnStr += "more stuff"
    for item in self.ledger:
      
    return returnStr


  def deposit(self, amount, description=""): # instance attribute, also called class method? #dict.self{"amount": amount, "description": description}
    #A deposit method that accepts an amount and description. If no description is given, it should default to an empty string. The method should append an object to the ledger list in the form of {"amount": amount, "description": description}.
    self.ledger.append({
      'amount': float(amount), 'description': description
    })
    self.balance += float(amount)

  #A withdraw method that is similar to the deposit method, but the amount passed in should be stored in the ledger as a 
  # negative number. If there are not enough funds, nothing should be added to the ledger. This method should 
  # return True if the withdrawal took place, and False otherwise
  def withdraw(self, amount, description=""): # instance attribute, also called class method?
    if self.check_funds(amount):
      ## Check funds says it's ok. 
      # Go do stuff.
      self.ledger.append({
      'amount': -float(amount), 'description': description
    })
      self.balance -= float(amount)
      return True
    else:
      ## ceck funds says it's NOT ok, not enough money.
      return False
      

#A transfer method that accepts an amount and another budget category as arguments. The method should add a 
# withdrawal with the amount and the description 
# "Transfer to [Destination Budget Category]". The method should then add a deposit to the other budget category 
# with the amount and the description
#  "Transfer from [Source Budget Category]". If there are not enough funds, nothing should be added to either 
# ledgers. This method should return True if the
#  transfer took place, and False otherwise.
  def transfer(self, amount, otherCat):# instance attribute, also called class method?
    ## does the class have enough money to do it? Check with check_fundas()
    if self.check_funds(amount):
      ## it DOES have enough money. 
      ## deposit the amount into the receiving class
      otherCat.deposit(amount, 'Transfer from ' + self.name)
      ## withdraw the money from the first class
      self.withdraw(amount, 'Transfer to ' + otherCat.name)
      return True
    else:
      ## it does NOT have enough money.
      return False


#A get_balance method that returns the current balance of the budget category based on the deposits and withdrawals 
# that have occurred.
  def get_balance(self):
    return self.balance

#A check_funds method that accepts an amount as an argument. It returns False if the amount is greater than the balance 
# of the budget category and returns True otherwise. This method should be used by both the withdraw method and transfer method.
  def check_funds(self, amount): # instance attribute, also called class method?
    if amount > self.balance:
      return False
    return  True


  #A check_funds method that accepts an amount as an argument. It returns False if the amount is greater than the balance 
  # of the budget category and returns True otherwise. This method should be used by both the withdraw method and transfer 
  # method.
  #Output = f"*************Food*************\ndeposit                 900.00\nmilk, cereal, eggs, bac -45.67\nTransfer 
  #to Entertainme -20.00\nTotal: 834.33"

def create_spend_chart(categories):
  pass


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

print(food)
print(clothing)
print(food.name, food.balance)
print(auto.name, auto.balance)
print(entertainment.name, entertainment.balance)
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