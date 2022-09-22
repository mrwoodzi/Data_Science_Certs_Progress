def __str__(self):
        returnStr = ""
        returnStr += self.name.center(30, '*') + '\n'
        for item in self.ledger:
            if len(item['description']) > 23:
                desc = item['description'][:23]
            else:
                desc = item['description'].ljust(23)
            lineAmount = format(item['amount'], '.2f').rjust(7)
            returnStr += desc + lineAmount + "\n"
        returnStr += "Total: " + str(self.get_balance())
        return returnStr




Below is for __str__:
    #f"*************Food*************\ndeposit                 900.00\nmilk, cereal, eggs, bac 
    # -45.67\nTransfer to Entertainme -20.00\nTotal: 834.33"
    line_num = 30
    len_self = len(self.name)
    name = str(self.name)
    #print(len_self)
    star_num = ((line_num - len_self)/2)
    stars = '*' * (int(star_num))
    line = f'{stars}{name}{stars}\n'
    space = """ """
    line = to_string