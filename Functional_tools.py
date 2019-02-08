# call functions on an iterable's items = MAP

from Lambda_funct import echo  # first, let me import that sweet print function

counters = [1, 2, 3, 4]
updated = []
for x in counters:
    updated.append(x + 10)

# can be reduced a lot by using map!
inc = lambda x: x + 10  # decided to use a lambda, no need for a full function for a simple return x+n
echo(list(map(inc, counters)))

# or even better:
echo(list(map((lambda x: x + 10), counters)))  # more refined version of above with lambda, neat


# instead FILTER and REDUCE select an iterable's items based on a test function and apply functions to item pairs
list(range(-5, 5))
echo(list(filter((lambda x: x > 0), range (-5, 5))))  # all values>0

# can easily be emulated by list comprehension syntax:
echo([x for x in range(-5, 5) if x > 0])

from functools import reduce

echo(reduce((lambda x, y: x + y), [1, 2, 3, 4]))