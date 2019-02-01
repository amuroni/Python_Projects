squares = [x ** 2 for x in [1, 2, 3, 4, 5]]
print(squares)

# or can be written as follows:

squares = []
for x in [1, 2, 3, 4, 5]:
    squares.append(x ** 2)
    # print(squares) bad idea!! this one prints the squares each time the loop runs
print(squares)  # this one instead, prints directly all the squared number in a list

# more iterators

D = {"a": 1, "b": 2, "c": 3}
for key in D.keys():
    print(key, D[key])

I = iter(D)
print(next(I))
print(next(I))
print(next(I))
# print(next(I)) this one would return error - stop iteration!

# btw we don't need to actually call the keys in the for loop
for key in D:
    print(key, D[key])

