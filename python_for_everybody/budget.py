# needs a ledger that is a list


class Category:
    ledger = [] #class atribute
    all = []
    def __init__(self, food=None, clothing=None, auto=None, entertainment=None, business=None): # magic method
        #Run Validations to the received arguments

        #Assign to self object
        self.food = food
        self.clothing = clothing
        self.auto = auto
        self.entertainment = entertainment
        self.business = business

        # Actions to execute
        Category.all.append(self)


    def deposit(self, deposit=float, sd=''):
        self.deposit = self.deposit
        pass
        #self.ledger(deposit, s)
        #return self.deposit

    def withdraw(self, withdraw=float, sw=''):
        self.withdraw = self.withdraw
        print(sw, withdraw)
        #withdraw = (withdraw/-1)
        pass
        #something possibly useful on oop py vid at 1hr 8min go double check
        #balance += (money/-1)
        #return self.withdraw

    #def auto(self, auto=float, sa=''):
        #print(sa)
        #print(str(auto))
        pass

    def get_balance(self):
        self.balance = self.deposit - self.withdraw
        return self.balance 


    def transfer(self, transfer, st=''):
        pass

    def check_funds(self, check_funds):
        pass
    
    def ledger(self): # instance variable, adds all transactions as a list
        pass

    def __repr__(self):
        return f"Category('{self.food}')"

#def create_spend_chart:

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
print(Category.all)

for instance in Category.all:
    print(instance.all)

