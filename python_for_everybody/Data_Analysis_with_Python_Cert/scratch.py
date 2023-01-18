squares = ['orange', 'orange', 'purple', 'blue ', 'orange']
new_squares = []

for colors in squares:
    if colors == 'orange':
        new_squares.append(colors)

print(new_squares)

squares = ['orange', 'orange', 'purple', 'blue ', 'orange']
new_squares = []
i = 0
while(i < len(squares) and squares[i] == 'orange'):
    new_squares.append(squares[i])
    i = i + 1
print (new_squares)