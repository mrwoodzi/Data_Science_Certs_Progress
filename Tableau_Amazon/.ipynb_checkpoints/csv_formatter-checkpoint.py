import csv 
op = open('listening.csv')
dt = csv.DictReader(op)
print(dt)