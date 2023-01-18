# for thing in data
#Set some variables to initial values
#Look for somethin or do something to each entry separately updating a variable
#Look at the variables

print('Before')
for thing in [9, 41, 12, 3, 74, 15]:
    print(thing)
print('After')

larget_so_far = -1
print('Largest So Far', larget_so_far)
for the_num in [9, 41, 12, 3, 74, 15]:
    if the_num > larget_so_far:
       larget_so_far = the_num
    print(larget_so_far, the_num)

print('The Largest Number Is?!?', larget_so_far, '!')

smallest = None
print("Before:", smallest)
for itervar in [3, 41, 12, 9, 74, 1, 15]:
    if smallest is None or itervar < smallest:
        smallest = itervar
    print("Loop:", itervar, smallest)
print("Smallest:", smallest)
