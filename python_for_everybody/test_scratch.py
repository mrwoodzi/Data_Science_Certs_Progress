my_dict = [{2:1, 3:1, 5:2}, {3:4, 6:4, 2:3}, {2:5, 3:6}]

# Finds the common keys
common_keys = set.intersection(*map(set, my_dict))

# Makes a new dict with only those keys and sums the values into another dict
print(common_keys)