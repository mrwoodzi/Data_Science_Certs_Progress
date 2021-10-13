# Dictionaries - A 'bag' of values, each with its own label
#Dictionaries are pythons most power data collection tool
#Allow us to do fast database-like operations
#Dictionaries have different names in different languages
    #Associative Arrays - Perl/php
    #Properties or Map or HashMap -Java
    #Property Bag-C#/.Net

purse = dict()
purse['money'] = 12
purse['candy'] = 3
purse['tissues'] = 75
print(purse)
print(purse['candy'])
purse['candy'] = purse['candy'] + 2 
print(purse)

# I missed this answer on free_code camp
dict = {"Fri": 20, "Thu": 6, "Sat": 1}
print(dict) 
dict["Thu"] = 13
dict["Sat"] = 2
dict["Sun"] = 9
print(dict) 
#>>>{'Fri': 20, 'Thu': 13, 'Sat': 2, 'Sun': 9}
#It changes the values in the keys that already exist and adds the new key:value pair {'Sun': 9}


#Dictionary Tracebacks
# you can use  'in'
#Dynamically adding values to a key
counts = dict()
names = ['csev', 'cwen', 'csev', 'zqian', 'cwen']
for name in names:
    if name not in counts:
        counts[name] = 1
    else:
        counts[name] = counts[name] + 1
print(counts)

