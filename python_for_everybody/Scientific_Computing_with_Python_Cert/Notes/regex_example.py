# Matching and Extracting Data
# re.search() returns a True/False depending on whether the string matches the regex
# re.findall() extracts the matching strings

# Greedy - returns the longest string because it's programmed that way
# ex. '^F.+:' 
#   First character in the match is an F
#   .+ is one or more charcters
#   : Ends with a colon
#   But returns only the largest string 

# Non-Greedy - returns the shortest string
# ex. '^F.+?:
# ? makes it non greedy

import re
x = "My 2 favorite numbers are 19 and 42 stephen.marquard@uct.ac.za"
y = re.findall('[0-9]+',x) # looks through string and pulls out anything with 1 or more digits
print(y)

y = re.findall('[AEIOU]+', x) # iterates over x and finds and pulls out any AEIOU, which there are none
print(y)


s = 'A message from csev@umich.edu to cwen@iupui.edu about meeting @2PM'
lst = re.findall('\\S+@\\S+', s)
print(lst)

y = re.findall('\S+@\S+' ,x) # goes greedy
print(y)

y = re.findall('^From (\S+@\S+)' ,x) # this didn't work right and printed nothing
print(y)

hand = open('mbox-short.txt')
numlist = list()
for line in hand:
    line = line.strip()
    stuff = re.findall('^X-DSPAM-Confidence: ([0-9.]+)', line)
    if len(stuff) != 1 : continue
    num = float(stuff[0])
    numlist.append(num)
print('Maximum:', max(numlist))

