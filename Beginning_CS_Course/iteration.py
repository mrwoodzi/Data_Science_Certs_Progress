the_numbers = [9, 41, 12, 3, 74, 15] # automatically classifies the list as integers
zork = 0
iter = 0 
print(f"Before the loop zork is {zork}")
for thing in [9, 41, 12, 3, 74, 15]: # thing is the iteration value
    zork = zork + 1
    print(f"Iteration {iter}: zork is now {zork}, the_numbers[{the_numbers[iter]}] is {thing}")
    iter = iter + 1
print(f'After the loop zork is {zork}')



# #adding
# zorklon = 0
# print('Before',  zorklon)
# for stuff in [9, 41, 12, 3, 74, 15]: # thing is the iteration value
#     zorklon = zorklon + stuff
#     print(zorklon, stuff)
# print('After', zorklon)

# #Finding Average
# count = 0
# sum = 0
# print('Before', count, sum)
# for value in [9, 41, 12, 3, 74, 15]: #value is the interation variable
#     count = count + 1
#     sum = sum + value
#     print(count, sum, value)
# print('After', count, sum, sum / count)

# #Filtering in a Loop
# print('Before')
# for numbers in [9, 41, 12, 3, 74, 15]:
#     if numbers > 20:            # the if statement filters the values
#         print('Large number', numbers)
# print('After')

# #Searching with a Boolean Variable

# found = False
# print('Before', found)
# for numbers in the_numbers: # numbers is the iteration variable
#     if numbers == 3:
#         found = True
#     print(found, numbers)
# print('After', found)

# #Finding the smallest value, this keeps us dealing with only the interation variables

# smallest = None
# print('Before', smallest)
# for value in the_numbers:
#     if smallest is None:
#         smallest = value
#     elif value < smallest:
#         smallest = value
#     print(smallest, value)
# print('After', smallest)