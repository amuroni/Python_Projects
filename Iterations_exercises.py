squares = [x ** 2 for x in [1, 2, 3, 4, 5]]
print(squares)

# or can be written as follows:

squares = []
for x in [1, 2, 3, 4, 5]:
    squares.append(x ** 2)
    # print(squares) bad idea!! this one prints the squares each time the loop runs
print(squares)  # this one instead, prints directly all the squared number in a list
