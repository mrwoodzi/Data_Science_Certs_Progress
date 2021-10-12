#List are mutable, meaning they can be changed
#can be changed with the index operator
# Python provides 'in'  and 'not in'

#Changing an item in a list
lotto = [2, 14, 26, 41, 63]
print(lotto)
lotto[2] = 28 # changes 26 to 28
print(lotto) 

# Finding out how long a list is
print(len(lotto))

#Finding range
print(range(len(lotto)))

friends = ['Joseph', 'Glenn', 'Sally']
for i in range(len(friends)):
    friend = friends[i]
    print('Happy New Year:', friend)

#Building a List from scratch
stuff = list() # tells python we have an empty that and python allows us to populate it later
stuff.append('book')
stuff.append(99)
print(stuff)

# Finding out if something is in a list
some = [2, 14, 26, 41, 63]
if 9 in some:
    print('False')
    
#Sorting a list
friends.sort()
print(friends)
print(friends[2])

#User populates a list and python gives back the average
numlist = list()
while True:
    inp = input('Enter a Number: ')
    if inp == 'done' : break 
    value = float(inp)
    numlist.append(value)

average = sum(numlist) / len(numlist)
print('Average:', average)



