smallest_so_far = None # we gave the program a number to start with
print('Before', smallest_so_far)
for the_num in [9, 41, 12, 3, 74, 15] :
    if smallest_so_far is None:  
        smallest_so_far = the_num
    elif the_num < smallest_so_far :
        smallest_so_far = the_num # it's remembering the largest number/storing it
    print(smallest_so_far, the_num)

print('After', smallest_so_far)