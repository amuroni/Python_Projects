even = [2, 4, 6, 8, 10]
odd = [1, 3, 5, 7, 9]

numbers = even + odd
numbers_in_order = sorted(numbers)

print("This list is not ordered: " + str(numbers))
print("This list is  ordered: " + str(numbers_in_order))
list_lenght = len(even) + len(odd)

print("Total numbers in both list is :" + str(list_lenght))
print()
print("Time do to some math now")
print("A. These nums are not in order")
for i in range(0, list_lenght):
        print(numbers[i],"", end="")
print()
print("B. These nums ARE in order"),
for i in range(0, list_lenght):
    print(numbers_in_order[i],"", end="")
print()
print("C. These are the ordered numbers, but squared")
totalsquarenumber = 0
for i in range(0, list_lenght):
    squarenumber = numbers_in_order[i]**2
    print(squarenumber, "", end="")
    totalsquarenumber = totalsquarenumber + numbers_in_order[i]**2
print()
print("And this are all square numbers summed up: " + str(totalsquarenumber))

# list comprehension - always written in square brackets

L = [1, 2, 3, 4, 5]
L = [x + 10 for x in L]
print(L)