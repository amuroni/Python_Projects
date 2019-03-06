# intercepting built-in operations in a class methods


class Number:
    def __init__(self, start):  # __init__.py basic op. ovld ->initialize class using any arguments passed
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


class C:
    def __index__(self):  # ths one returns an integer value for an instance
        return 255

# __getitem__ and index iteration


class StepperIndex:
    def __getitem__(self, i):
        return self.data[i]


X = StepperIndex()
X.data = "SPAM"
for item in X:
    print(item, end=" - ")

print()


class Squares:
    def __init__(self, start, stop):
        self.value = start - 1
        self.stop = stop

    def __iter__(self):  # iterator object on iter
        return self

    def __next__(self):  # return square on each iteration
        if self.value == self.stop:
            raise StopIteration
        self.value += 1
        return self.value ** 2


for i in Squares(1,5):
    print(i, end=" ")
print()


# a lot easier like this anyway
def gsquares(start, stop):
    for i in range(start, stop+1):
        yield i**2


for i in gsquares(1, 5):
    print(i, end=" ")
print()

# or even easier:
for i in (x ** 2 for x in range(1, 6)):
    print(i, end=" ")
print()

# or the fastest version:

print([x**2 for x in range(1,6)])

print("*******")
