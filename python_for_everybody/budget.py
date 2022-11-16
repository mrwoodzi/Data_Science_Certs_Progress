import math
import re

class Category:
  def __init__(self, name): # magic method/dunder method
    self.name = name # instance attribute
    self.ledger = [] # instance variable
    self.d = {} # instance variable
    self.balance = 0 # instance variable
    self.wd = 0

  def __str__(self): # Instance method
    returnStr = ""
    returnStr += self.name.center(30, '*') + '\n'
    for a, b in self.d.items():
      returnStr +=  "{:<23}".format(a[:23]) + str(b).rjust(7) + '\n'
    returnStr += 'Total: '.ljust(2) + str(self.balance).rjust(2)
    return returnStr
  

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
      self.wd += float(amount)
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

  # Can I make a def percentage to pass to spend_chart?


def create_spend_chart(args): # How do I put in multiple args since *args not working
  # Total withdraws in all Categories divided by total withdraw added up in all categories
  # left side of chart should be label 1-100 in 10s
  # lside += None
  # bars on bar chart should be "o"
  # bside += None
  # each bar is rounded down to the nearest 10 
  # horizontal line should go go 2 spaces past final bar in bar chart
  # hline_ += None
  # each category name should be written vertically
  # cat_name += None
  total = 0
  percent_count = 100
  lines = "-"
  spend_chart = "Percentage spent by category\n"
  cat_percent_d = {}
  len_biggest_cat = 0
  cat_str = ""
  cat_ints = []
  cat_split = []
  no = ""
  ni = ""
  nt = ""

  for a in args: # we acces self.withdraw
    total += int(a.wd) # make a total of all withdraw

  for arg in args: # get name and amount of withdraws in each class and the get percent
    cat_percent_d[f"{arg.name}"] = [(math.trunc((arg.wd)/(total)*10)*10)] # don't need at the moment
    cat_str += arg.name
    cat_ints += str((math.trunc((arg.wd)/(total)*10)))
    print(cat_ints)
    print(arg.name)
    print(len(arg.name))
    print(len_biggest_cat)
    if (len(arg.name)) > len_biggest_cat: # identifying and storing longest len category
      len_biggest_cat = len(arg.name)
      print(len_biggest_cat)
      
  
  len_cat_keys = len(cat_str) 
  cat_split = re.findall('[A-Z][^A-Z]*', cat_str)
  len_cat_split = len(cat_split)
  
  # This prints the top half of the bar chart
  oo = int(cat_ints[0])
  oi = int(cat_ints[1])
  ot = int(cat_ints[-1])
  while percent_count >= 0:
    if int(oo) < (percent_count/10):
      op = "".ljust(1)
    elif int(oo) >= (percent_count/10):
      op = "o"
    if int(oi) < (percent_count/10):
      ip = "".ljust(1)
    elif int(oi) >= (percent_count/10):
      ip = "o"
    if int(ot) < (percent_count/10):
      tp = "".ljust(1)
    elif int(ot) >= (percent_count/10):
      tp = "o"
    spend_chart += f"{percent_count}|".rjust(4, " ") + f" {op}  {ip}  {tp}  \n"
    percent_count -= 10
  spend_chart += "".ljust(4) + "".rjust(10, f"{lines}") + "\n" # need to figure out the len of lines


  # Splitting Categories into separate lists
  for v in cat_split[0]:
    no += v
  for v in cat_split[1]:
    ni += v
  for v in cat_split[2]:
    nt += v
  print(len_biggest_cat)

  # Getting Character Lengths the same for iteration
  if len(no) <= len_biggest_cat:
    if len(no) == len_biggest_cat:
     no = no.ljust(len_biggest_cat)
    elif len(no) < len_biggest_cat:
      no = no.ljust(len_biggest_cat-(len(no)))
  if len(ni) <= len_biggest_cat:
    if len(ni) == len_biggest_cat:
     ni = ni.ljust(len_biggest_cat)
    elif len(ni) < len_biggest_cat:
      ni = ni.ljust(len_biggest_cat-(len(ni)))
  if len(nt) <= len_biggest_cat:
    if len(nt) == len_biggest_cat:
     nt = nt.ljust(len_biggest_cat)
    elif len(nt) < len_biggest_cat:
      nt = nt.ljust(len_biggest_cat-(len(nt)))
  
  # while len_biggest_cat > 0:
  for a,b,c in zip(no, ni, nt):
    spend_chart += f"     {a}  {b}  {c}  \n".rjust(9, " ")

  return spend_chart






food = Category("Food") #category
entertainment = Category("Entertainment")
business = Category("Business")
auto = Category("Auto") #category
clothing = Category("Clothing") #category        
food.deposit(900, "deposit")
entertainment.deposit(900, "deposit")
business.deposit(900, "deposit")
food.withdraw(105.55)
entertainment.withdraw(33.40)
business.withdraw(10.99)
print(create_spend_chart([business, food, entertainment]))
