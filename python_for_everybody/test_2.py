A = ['blue', 'green', 'green', 'green']
B ={"blue": 2,"red": 1}

if sum(B[k] for k in A if k in B):
    print("sum higher than 10")
else:
    print("sum lower than 10")

