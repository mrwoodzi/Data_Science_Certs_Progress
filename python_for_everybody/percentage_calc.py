
# I wrote this by myself not because it was apart of an example but since I needed to figure some percentages 
percentage = input("Input Percentage in decimals: ")
number     = input("Input Number: ")

p = float(percentage)
n = float(number)

percent  = ((p * n) - n) * -1.0 

print(f"Your percentage of the input number is {percent}")


