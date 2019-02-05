# sum of numbers in a nested sublist structure

L = [1, [2, [3, 4], 5], 6, [7, 8]]  # AKA arbitrary nesting - non-linear


def sumtree(L):
    tot = 0
    for x in L:                      # for each x in list L
        if not isinstance(x, list):  # check if obj x is a list
            tot += x                 # if a list, add numbers directly
        else:                        # if not a list,
            tot += sumtree(x)        # recur for other sublists
    return tot


print(sumtree(L))  # total is 36


# another solution, with a FIFO method
def sumtree2(L):
    tot = 0                              # like previous func, BUT
    items = list(L)                      # uses an explicit list
    while items:
        front = items.pop(0)             # fetch front item first
        if not isinstance(front, list):  # if a list
            tot += front                 # add nums directly
        else:                            # if not
            items.extend(front)          # append to nested list
    return tot


print(sumtree2(L))  # tot still 36


# another solution, with a LIFO method
def sumtree3(L):
    tot = 0                              # like previous func, BUT
    items = list(L)                      # uses an explicit list
    while items:
        front = items.pop(0)             # fetch front item first
        if not isinstance(front, list):  # if a list
            tot += front                 # add nums directly
        else:                            # if not
            items[:0] = front            # prepend all in nested list
    return tot


print(sumtree3(L))  # tot still 36
