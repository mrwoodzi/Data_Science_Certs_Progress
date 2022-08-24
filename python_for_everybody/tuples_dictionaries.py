# Parenthesis 
#Tuples are immutable
# >>> z = (5, 4, 3)
# >>> z[2] = 0 you can not reassign a variable in a tuple and you will get a 
# Traceback: 'tuple object does not support item assignment
# Tuples are limited Lists
# Super Cool you can have a tuple on the left-hand side of an assignment statement
# Tuples can be compared but only checks the first variable*******
    # it only looks at things chronologically *******
# (0, 1, 2) < (5, 1, 2)
# True
# ( 0, 1, 200000000) < (0, 3, 4)
# True
# ('Jones', 'Sally') < ('Jones', 'Sam')
# True
# ('Jones', 'Sally') > ('Adams', 'Sam')
# True 

(x, y) = (4, 'fred')
print(y)

(a, b) = (99, 98)
print(a)

#
d = dict()
d['quincy'] = 1
d['beau'] = 5
d['kris'] = 9
for (k,i) in d.items():
    print(k, i)

tups = d.items() # prints the new compiled key:value pairs in the dictionary d 
print(tups)

# Sorting List of Tuples and then putting them into dict
# sort them with items() and sorted() function
# Sorts them by their key and not the value
# You can sort by values, see below

# >>>m = {'a':10, 'b':1, 'c':22}
# >>>m.items()
# dict_items([('a', 10), ('c', 22), ('b', 1)])
# >>>sorted(m.items())
# [('a', 10), ('b', 1), ('c', 22)] 

 # Sorting by Value instead of key
# Swap the k,v pair to v,k and then sort 
# Do this with a for loop
c = {'a':10, 'b':1, 'c':22}
tmp = list() # this puts them in a temporary list
for  k, v in c.items(): 
    tmp.append((v,k)) # this swaps k, v to v, k

print(tmp)
tmp = sorted(tmp, reverse=True) # reverse=True puts the highest v, k first in the list
print(tmp)

# The top 10 most common words