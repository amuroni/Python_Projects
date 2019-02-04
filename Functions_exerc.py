# used to maximize code reuse and minimize redundancy


def times(x, y):
    return x * y


print(times(2, 4))
x = round(times(15.425, 3))
print(x)
print(times("A", 4))


def intersect(seq1, seq2):  # not an optimal function anyway, see below for an alternative
    res = []  # a list [], and not a tuple () since it cannot have a .append (immutable obj)
    for x in seq1:
        if x in seq2:
            res.append(x)
    return res


s1 = "SPAM"
s2 = "SCAM"

compare = intersect(s1, s2)
print(compare)

# alternative function

compare2 = [x for x in s1 if x in s2]  # same result with shorter code
print(compare2)

y = intersect([1, 2, 3], (1, 4))  # functions are polymorphic - works with mixed and arbitrary types no problem
print(y)

# Global Scope
X = 99


def func(Y):  # local scope
    Z = X + Y  # Y and Z are local since assigned in the function, X is still global
    return Z


print(func(1))


def makeActions():
    acts = []
    for i in range(5):
        acts.append(lambda x, i=i: i ** x)  # i=i to remember the current i variable
    return acts


acts = makeActions()
print(acts[0](2))


def changer(a, b):  # assigns the arguments a and b
    a = 2           # changes local name's value ONLY - no effect on the caller below
    b[0] = "spam"   # changes shared object in place 0


K = 1               # not affected by the local call in the changer func
L = [1, 2]          # <- CALLER
changer(K, L)       # Pass immutable and mutable objects
print(K, L)         # This returns 1 ["spam", 2] - K is still 1, L is different!

print("_____________")


def func(spam, eggs, toast=0, ham=0):  # first 2 are required for the function to work
    print((spam, eggs, toast, ham))    # 3rd and 4th can be omitted (default= 0)


func(1, 2)
func(1, ham=1, eggs=0)
func(spam=1, eggs=0)
func(toast=1, eggs=2, spam=3)
func(1, 2, 3, 4)
print("_____________")


def f(*args): print(args)  # collects all arguments in a tuple object


f()
f(1)


def f2(**args): print(args)  # collects arguments into a dictionary object


f2()
f2(a=1, b=2)
print("_____________")

# The MIN exercise with functions:
# code a function that is able to compute the minimum value from
# an arbitrary set of arguments and an arbitrary set of object data types


def min1(*args):
    res = args[0]
    for arg in args[1:]:  # compares the first argument with the others by slicing the array with [1:]
        if arg < res:     # if it's the lowest one
            res = arg     # result is = to the lower arg
    return res


print(min1(3, 4, 1, 2, 10, 5, 9))  # compares the 3 with all other args, returns 1
print("****")


def min2(first, *rest):
    for arg in rest:
        if arg < first:  # no need to slice, lets Python sort the rest of the args comparing the first
            first = arg
    return first


print(min2(3, 4, 1, 2, 10, 5, 9))
print(min2("bb", "aa", "cc", "dd", "a"))
print("****")


def min3(*args):      # probably the best one
    tmp = list(args)  # converts the arguments in a list
    tmp.sort()        # lets Python sort the list
    return tmp[0]     # returns the first value in position 0, which is the lowest one


print(min3(3, 4, 1, 2, 10, 5, 9))
print(min3("bb", "aa", "cc", "dd", "a"))
print(min3([2, 2], [1, 1], [3, 3], [5, 5], [0, 1]))
print("****")


def max1(*args):
    tmp = list(args)  # converts the arguments in a list
    tmp.sort()        # lets Python sort the list
    return tmp[-1]    # returns the LAST value of the list aka [-1], the max one


print(max1(3, 4, 1, 2, 10, 5, 9))
print(max1("bb", "aa", "cc", "dd", "a"))
print(max1([2, 2], [1, 1], [3, 3], [5, 5], [0, 1]))
print("****")

# generalize a function to compute either a min or max value


def minmax(test, *args):  # main function to determine the result and the args tuple
    res = args[0]
    for arg in args[1:]:
        if test(arg, res):
            res = arg
    return res


def lessthan(x, y): return x < y  # test parameter for min arg


def grtrthan(x, y): return x > y  # test parameter for max arg


print(minmax(lessthan, 4, 2, 1, 5, 6, 3))  # with *args, everything after test, is a tuple
print(minmax(grtrthan, 4, 2, 1, 5, 6, 3))

# btw, max and min are both python built-ins, so no need for custom functions!!
print("****")

# here is an intersect function for fun, just because we can do it


def intersect(*args):                 # intersects one or more sequences
    res = []                          # initial list is empty
    for x in args[0]:                 # scans first sequence
        if x in res:                  # checks for duplicates
            continue                  # skip if it is a duplicate
        for other in args[1:]:        # if not, for other args
            if x not in other:        # item in both?
                break                 # NO, then break out of loop
        else:                         # if yes
            res.append(x)             # add item at the end of res list obj
    return res                        # return the list of intersects


print(intersect([1, 2, 3, 4], (1, 4)))  # returns [1, 4]

# we can also do an union function with the same mechanism

def union(*args):
    res =[]                          # empty list to start
    for seq in args:                 # for each sequence
        for x in seq:                # for each sequence value
            if x not in res:         # if it's not in list res
                res.append(x)        # append to the list
    return res                       # return the list


print(union([1, 2, 3, 4], (1, 4)))  # returns [1, 2, 3, 4]
print("****")
print(intersect(s1, s2), union(s1, s2)) #returns SAM end SPAMC
print("****")
