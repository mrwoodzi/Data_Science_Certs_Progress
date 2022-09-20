skuArray = [('000381001238',), ('000381001238',), ('000381001238',), ('FA200513652',), ('000614400967',)]
new = ', '.join(["'{}'".format(x[0]) for x in skuArray])

print(skuArray)
print(new[0])
