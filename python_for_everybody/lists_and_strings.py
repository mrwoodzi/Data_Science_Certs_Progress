# Puts the string into a list
abc = 'With three words'
stuff = abc.split()
upper = abc.upper()
print(stuff)
print(len(stuff))
print(stuff[0])
for w in stuff:
    print(w)
print(upper)


#This gets rid of all spaces and puts into a List
line = 'A lot                  of spaces'
etc = line.split()
print(etc)


#This seems it all as one item in a List
line1 = 'first;second;third'
thing = line1.split()
print(thing)
print(len(thing))


#We specify what to be removed with 'split'
thing = line1.split(';')# technically a delimiter
print(thing)
print(len(thing))

fhand = open('mbox.txt')
for line in fhand:
    line = line.rstrip()
    if not line.startswith('But ') : continue
    words = line.split()

# Double Split Pattern
line = 'From stephen.marquard@uct.ac.za Sat  Jan  5 09:14:16 2008'
words = line.split()
email = words[1]
print(email)
email_name = email.split('@')
print(email_name[0])

