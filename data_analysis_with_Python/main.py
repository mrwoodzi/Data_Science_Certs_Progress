import numpy as np

new_matrix = np.array([[1, 2, 3], 
                       [4, 5, 6], 
                       [7, 8, 9]
                       ])

print(new_matrix)
nm_sum = new_matrix.sum(axis=0) # adds y axis for all
print(nm_sum)

a = np.arange(5)
a + 20
print(a)