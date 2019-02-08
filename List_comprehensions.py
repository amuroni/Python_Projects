# why list comprehensions are so powerful

# one could write this:

print([x**2 for x in range(10)])  # simple, readable, easy
# OR
print(list(map((lambda x: x**2), range(10))))  # here we need to use a lambda instead of a def

print([x for x in range(17) if x % 2 == 0])
# which is a bit more intricate with a lambda
print(list(filter((lambda x: x % 2 == 0), range(17))))
# and even worse with a for
res = []
for x in range(17):
    if x % 2 == 0:
        res.append(x)
print(res)

# and we can also combine both filter and map, see:
print([x ** 2 for x in range(17) if x % 2 == 0])
# instead of this abomination
print(list(map((lambda x: x**2), filter((lambda x: x % 2 == 0), range(17)))))

print("*****************")

# we can also write less verbose code, like:

res = [x + y for x in [0, 1, 2] for y in [100, 200, 300]]
print(res)

# and we can add even more inside;
res2 = [x + y for x in range(10) if x % 2 == 0 for y in range(5) if y % 2 == 1]
print(res2)
print("*****************")
# let's use matrixes

M = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]
print([M[i][i] for i in range(len(M))])  # diagonal ULtoLR
print([M[i][len(M)-1-i] for i in range(len(M))])  # diagonal URtoLL

# and we can also extend the matrix, see

M2 = [[col + 9 for col in row] for row in M]
M.append(M2)
print(M)
