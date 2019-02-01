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

y = intersect([1, 2, 3], (1, 4))  # function are polymorphic - works with mixed and arbitrary types no problem
print(y)
