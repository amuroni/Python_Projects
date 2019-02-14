# generator functions -> coded as a def but use YIELD statement to return one at a time
# generator expression -> comprehension expression enclosed in parenthesis

def gensquares(n):
    for i in range(n):
        yield i ** 2

for i in gensquares(5):
    print(i, end=" : ")

# alternatively it would've been as follows
print()


def buildsquares(n):
    res = []
    for i in range(n): res.append(i ** 2)
    return res

for x in buildsquares(5): print(x, end=" : ")
print() #or
for x in [n **2 for n in range(5)]:
    print(x, end=" : ")
print() #OR
for x in map((lambda n: n**2), range(5)):
    print(x, end=" : ")

print()
# generators are better in memory use and performance

def ups(line):
    for sub in line.split(","):
        yield sub.upper()


print(tuple(ups("aaa, bbb, ccc, ddd")))

# generator expressions

x = [x**2 for x in range(4)]  # list comprehension
list(x**2 for x in range(4))  #generator expression -> make an iterable!

for num in (x**2 for x in range(4)):
    print("%s, %s" % (num, num / 2.0))

# generators vs map function

list(map(abs, (-1, -2, -3, -4)))
#or
list(abs(x) for x in (-1, -2, -3, -4))

list(map(lambda x: x+2, (1, 2, 3, 4)))
#or
list(x*2 for x in (1, 2, 3, 4))

# nested generator with map

import math
list(map(math.sqrt, (x++2 for x in range(4))))  # nested combination!


# generator vs filter

line = "a bbbb c dd ee f"
print("".join(x for x in line.split() if len(x)>1))  # skips a and c since = 1 char
# could be done similar with filter function
print("".join(filter(lambda x: len(x)>1, line.split())))  # same result, more intricate


# scrambled sequences

def scramble(seq):
    for i in range(len(seq)):
        seq = (seq[i:] + seq[:i])
        yield seq                  # a lot more memory efficient

print(list(scramble("spam")))

for x in scramble((1, 2, 3)):      # and also works with for loops
    print(x, end=" ")

print()

# how to generalize a generator expression
F = lambda seq: (seq[i:] + seq[:i] for i in range(len(seq)))
print(list(F((1, 2, 3))))
# or
for x in F((1, 2, 3)):
    print(x, end=" ")

print()

# reduce memory and footprint
import math
print(math.factorial(10))  # = 3628800

def permute1(seq):
    if not seq:
        return [seq]                        # Empty sequence
    else:
        res = []
        for i in range(len(seq)):
            rest = seq[:i] + seq[i+1:]      # Delete current node
            for x in permute1(rest):        # Permute the others
                res.append(seq[i:i+1] + x)  # Add node at front
    return res

def permute2(seq):
    if not seq:           # Shuffle any sequence: generator
        yield seq         # Empty sequence
    else:
        for i in range(len(seq)):
            rest = seq[:i] + seq[i+1:]  # Delete current node
            for x in permute2(rest):    # Permute the others
                yield seq[i:i+1] + x


#seq = (list(range(10)))
#p1 = permute1(seq)
#print(permute1(seq))  #took a hell of a long time, not optimal!

import random
print(math.factorial(20)) # super quick

seq = list(range(20))
random.shuffle(seq)
p = permute2(seq)
print(next(p))

# let's see how expressive generators can be

S1 = "abc"
S2 = "xyz123"
list1 = list(zip(S1, S2))
print(list1)

list2 = list(zip([1, 2, 3, 4, 5, 6], [2, 3, 4, 5, 6]))
print(list2)


list3 = list(map(pow, [1, 2, 3,], [2, 3, 4]))
print(list3)    # result = 1^2, 2^3, 3^4


def mymap(func, *seqs):
    res = []
    for args in zip(*seqs):      # collects multiple sequence args
        res.append(func(*args))  # appends the func + arg
    return res                   # return as a list


print(mymap(abs, [-1, -1, 0, 1, 2]))
print(mymap(pow, [1, 2, 3], [2, 3, 4]))


def myzip(*seqs):
    seqs = [list(S) for S in seqs]
    while all(seqs):
        yield(tuple(S.pop(0) for S in seqs))



def mymapPad(*seqs, pad=None):
    seqs = [list(S) for S in seqs]
    while any(seqs):
        yield(tuple((S.pop(0) if S else pad) for S in seqs))


print(list(myzip(S1, S2)))
print(list(mymapPad(S1, S2)))
print(list((mymapPad(S1, S2, pad=99))))

