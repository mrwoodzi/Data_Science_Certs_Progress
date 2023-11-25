the_numbers_list = [9, 41, 12, 3, 74, 15] # automatically classifies the list as integers
number_of_iterations = 0
iter = 0 # iter has to start at 0 since the list starts at index 0
print(f"Before the loop number_of_iterations is {number_of_iterations}")
for iterating_the_numbers in the_numbers_list: # thing is the iteration value
    number_of_iterations = number_of_iterations + 1
    print(f"Iteration index {iter}: number_of_iterations is now {number_of_iterations}, first element in the_numbers list is {iterating_the_numbers}")
    iter = iter + 1
print(f'After the loop number_of_iterations is {number_of_iterations}')



# #adding
# number_of_iterationslon = 0
# print('Before',  number_of_iterationslon)
# for stuff in [9, 41, 12, 3, 74, 15]: # thing is the iteration value
#     number_of_iterationslon = number_of_iterationslon + stuff
#     print(number_of_iterationslon, stuff)
# print('After', number_of_iterationslon)

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