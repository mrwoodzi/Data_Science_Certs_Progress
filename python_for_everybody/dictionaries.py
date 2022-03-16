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
for x in names:
    if x not in counts:
        counts[x] = 1 #this adds a new name and starts a count
    else:
        counts[x] = counts[x] + 1 #this adds a count to the name that is already there
print(counts)


#Below code does the same as the above code
#The 'get' method for dictionaries
#You can use 'get()' and provide a default value of zero when the key is not yet in the dictionary
counts = dict()
names = ['csev', 'cwen', 'csev', 'zqian', 'cwen']
for x in names:
   counts[x] = x.get(name, 0) + 1
print(counts)


#This was the test question for Common Applications
# I didn't get it at first but
#print .get asks if 'kris is in the dictionary, it doesn't so it returns a 0
counts = { 'quincy' : 1 , 'mrugesh' : 42, 'beau': 100, '0': 10}
print(counts.get('kris', 0))


#*******************Dictionaries and Loops***************

name = input('Enter Filename: ')
handle = open(name)

counts = dict()
for line in handle:
    words = line.split()
    for word in words:  #nested loop
        counts[word] = counts.get(word, 0) + 1
    
bigcount = None
bigword = None
for word, count in counts.item():
    if bigcount is None or count > bigcount: # max loop
        bigword = word
        bigcount = count

print(bigword, bigcount)

#you can have 2 interation variables
jjj = {'jan' : 100, 'chuck' : 1, 'fred' : 42}
for aaa,bbb in jjj.items():
    print(aaa, bbb)