#File Processing

# Have to open file with "Open"
 # handle = open(filename, mode) 
 #fhand = open('mbox.txt', 'r')

 # opens into a handle where you can then do something with it

 # Escape Characters
    # Newline Character - \n

#Files as a sequence
#using for loop to read individual lines

xfile = open('mbox.txt')
for cheese in xfile:
    print(cheese)

#Reading the number of lines in a file
fhand = open('mbox.txt')
count = 0
for line in fhand:
    count = count + 1
print('Line Count:', count)

#Reading the Whole File
bhand = open('mbox.txt')
inp = bhand.read()
print(len(inp))
print(inp[:20])

# Searching Through a File
ahand = open('mbox.txt')
for line in ahand:
    line = line.rstrip() # This gets rid of whitespace
    if line.startswith('But'):
        print(line)

#We are skipping certain lines, does same as above
ahand = open('mbox.txt')
for line in ahand:
    line = line.rstrip() # This gets rid of whitespace
    if not line.startswith('But'):
        continue
    print(line)

#Using 'in' to select lines
dhand = open('mbox.txt')
for line in dhand:
    line = line.rstrip()
    if not 'But' in line:
        continue
    print(line)


