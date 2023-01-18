 # removing whitespace at the begginning or end of a string
 #lstrip() and rstrip() remove whitespace at the left or right
 #strip() removes both beginning and ending whitespace

greet = '   Hello Bob  '
real_great = greet.lstrip()
print(real_great)

dude = '        What up my man'
print(dude.lstrip())