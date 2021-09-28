n = 5
while n > 0:
    print (n)
    n = n - 1
print('Blastoff!')

# Below is a zero trip loop
x = 0
while n > 0:
    print('Lather')
    print('Rinse')
print('Dry Off!')

#breaking out of a looop

 # break says get out of loop
 # continue goes back to the top of loop

while True:
    line = input('> ')
    if line[0] == '#':
        continue
    if line == 'done' :
        break
    print(line)
print('Done!')
 





