# use arguments for inputs and return for outputs
# use global variables only when truly necessary
# don't change mutable args, unless expected
# each function -> single, unified purpose
# small size, if too long: split them

# EXAMPLE: next one is a badly coded sum function:


def mysum(L):
    if not L:                       # if the list is empty,
        return 0                    # return 0
    else:                           # if there are still values,
        return L[0] + mysum(L[1:])  # sum value in L[0] & the rest on the right = [1:]


print(mysum([1, 2, 3, 4, 5]))  # = 15; list smaller at each level until empty.


def mysum2(L):
    print(L)                        # Trace recursive levels
    if not L:                       # L shorter at each level
        return 0                    # the recursive loop ends with zero: the list is empty []
    else:
        return L[0] + mysum2(L[1:])


print(mysum2([1, 2, 3, 4, 5]))  # still 15, but in decremental steps until list is []

# BETTER ALTERNATIVES


# 1
def mysum_A(L):
    return 0 if not L else L[0] + mysum_A(L[1:])  # use of ternary expression


# 2
def mysum_B(L):
    return L[0] if len(L) == 1 else L[0] + mysum_B(L[1:])  # too elaborate imho


# 3
def mysum_C(L):
    first, *rest = L
    return first if not rest else first + mysum_C(rest)  # external sequence assignnment, NEAT!


# example of indirect recursion

def mysum3(L):
    if not L: return 0
    return nonempty(L)           # call a function that calls mysum3


def nonempty(L):
    return L[0] + mysum3(L[1:])  # indirectly recursive!


print(mysum([1.1, 2.2, 3.3, 4.4]))  # = 11.0

# let's make all of this a lot easier now with simple LOOPS

K = [1, 2, 3, 4, 5]
sum = 0
while K:
    sum += K[0]
    K = K[1:]
print(sum)

# or even easier with a simple for __ in __

for x in K: sum += x
print(sum)
