"""This is a setwrapper function.
It uses methods and has basic operator overloading,
and wraps a a python list with extra set operations."""


class Set:  # class
    def __init__(self, value=[]):  # constructor
        self.data = []  # manages list
        self.concat(value)

    def intersect(self, other):  # other = any sequence
        res = []
        for x in self.data:
            if x in other:  # pick common items
                res.append(x)
        return Set(res)  # return new set list

    def union(self, other):
        res = self.data[:]
        for x in other:  # add items in order!
            if x not in res:
                res.append(x)
        return Set(res)

    def concat(self, value):
        for x in value:  # another way of removing duplicates
            if x not in self.data:
                self.data.append(x)

    def __len__(self):
        return len(self.data)

    def __getitem__(self, key):
        return self.data[key]

    def __and__(self, other):
        return self.intersect(other)

    def __or__(self, other):
        return self.union(other)

    def __repr__(self):
        return "Set:" + repr(self.data)

    def __iter__(self):
        return iter(self.data)


# example

x = Set([1, 3, 5, 7])
print(x.union(Set([1, 4, 5, 9])))  # list merge
print(x | Set([1, 4, 6, 2]))  # append to list diff items

"""here is another version of the set class using the built-in list superclass"""


class Set2(list):
    def __init__(self, value=[]):  # constructor
        list.__init__([])  # customize list
        self.concat(value)  # copies mutable defaults

    def intersect(self, other):  # almost unchanged from previous version
        res = []
        for x in self:  # no need for self.data, not in main constructor
            if x in other:  # pick common items
                res.append(x)
        return Set(res)  # return new set list

    def union(self, other):
        res = Set(self)
        res.concat(other)
        return res

    def concat(self, value):
        for x in value:
            if x not in self:
                self.append(x)

    def __and__(self, other): return self.intersect(other)

    def __or__(self, other): return self.union(other)

    def __repr__(self): return 'Set:' + list.__repr__(self)


if __name__ == "__main__":
    x = Set([1, 3, 5, 7, 9, 11])
    y = Set([2, 1, 4, 5, 6, 7, 8, 9, 10, 12, 17])
    print(x, y, len(x), len(y))
    print(x.intersect(y), y.union(x))
    print(x & y, x | y)
