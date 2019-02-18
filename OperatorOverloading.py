# intercepting built-in operations in a class methods


class Number:
    def __init__(self, start):  # __init__ basic op. ovld ->initialize class using any arguments passed
        self.data = start

    def __sub__(self, other):   # __sub__ intercepts subtraction expressions and return new class with result
        return Number(self.data - other)


x = Number(5)
y = x - 2
print(y.data)


# __getitem__ -> slice expression
L = [5, 6, 7, 8, 9]
print(L[1:4])  # is a slice of L
L[slice(2, 4)]  # is also a slice of L, with the slice objects

# using the method instead


class Indexer:
    data = [5, 6, 7, 8, 9]

    def __getitem__(self, index):   # call for index or slice
        if isinstance(index, int):  # test type of the arguments
            print("indexing", index)
        else:
            print("slicing", index.start, index.stop, index.step)  # perform index/slice


x = Indexer()  # assign the indexer to a variable
print(x[0])  # returns value 5
print(x[1])  # returns value 6
print(x[-1])  # returns value 9
