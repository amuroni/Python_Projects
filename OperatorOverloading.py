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