# int(false) this equals 0
# int(true) this equals 1
# x = 2/2 # this prints a float


# For loop example

dates = [1982,1980,1973]
N = len(dates)

for i in range(N): # You access all values in list 
    print(dates[i])   
    
for year in dates:  # You also access all values in list
    print(year) 
    
for a in range(-4, 5): # this apparently works in pandas but not in VS Code
    print(a)
    
PlayListRatings = [10, 9.5, 10, 8, 7.5, 5, 10, 10]
a = 0
ratings = PlayListRatings[0]

while(a < len(PlayListRatings) and ratings >= 6):
    print(ratings)
    a = a + 1
    ratings = PlayListRatings[a]
    
dates = [1982, 1980, 1973, 2000]
i = 0
year = dates[0]

while(year != 1973):    
    print(year)
    i = i + 1
    year = dates[i]
    
print("It took ", i ,"repetitions to get out of loop.")

# While loop to print 'orange' and then stop when it's no longer 'orange'
squares = ['orange', 'orange', 'purple', 'blue ', 'orange']
new_squares = []
i = 0
while(i < len(squares) and squares[i] == 'orange'):
    new_squares.append(squares[i])
    i = i + 1
print (new_squares)

# What does a method do to an object? changes or interacts with the object

RedCircle=Circle(10,'red')
RedCircle.radius=1
#radius ends up being 1

BlueCircle=Circle(10,'blue')
BlueCircle.add_radius(20)
#radius adds to 30