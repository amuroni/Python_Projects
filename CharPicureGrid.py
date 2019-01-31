grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

for x in range(0, 6):
        for y in range(0, 9):
                print(grid[y][x], end="")
        print()



# rows = len(grid) # Number of elements in the list
# cols = len(grid[0]) # Number of elements in every single element in the list
#
# for j in range(cols):
#         for i in range(rows):
#                 print(grid[i][j], end='')
#         print()

# print(rows)
# print(cols)
