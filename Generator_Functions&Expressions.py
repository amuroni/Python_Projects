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


