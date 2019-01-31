M = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]

print(M[1])

col2 = [row[1] for row in M]  # collect items in column 2
print(col2)

print([row[1] + 1 for row in M])  # add 1 to each item in column 2

print([row[1] for row in M if row[1] % 2 == 0])  # filters ODD items (in this case n.5)

diag = [M[i][i] for i in [0, 1, 2]]
print(diag)

doubles = [c * 2 for c in col2]  # doebles values in col 2; c = value in row
print(doubles)

# generator below

G = (sum(row) for row in M)
print(next(G), end=", ")  # = 6, or the sum of first row in M
print(next(G), end=", ")  # = 15, or the sum of second row in M
print(next(G), end="")  # = 24, or the sum of third row in M
print()

map_func = list(map(sum, M))
print(map_func)  # same result as before, only with map, and returns a list

# how to create SETS from data of a matrix

set_M = {sum(row) for row in M}
print(set_M)

# how to create DICTIONARIES from data of a matrix

dict_sums_M = {i: sum(M[i]) for i in range(3)} # creates key: value for row sums
print (dict_sums_M)

