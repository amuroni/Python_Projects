#  lambda is a single expression, not a statement
# lambda similar to a def function with a return statement


def echo(arg):
    print(arg)

f = lambda x, y, z: x + y + z
print(f(2, 3, 4))

x = (lambda a = 1, b = 2, c = 3 : a + b + c)
print(x(4))  # 4 replaces the first values, so 4+2+3

# lambda is useful to nest functions, but with basic content

def knights():
    title = "Sir"
    action = (lambda x: title + " " + x)
    return action

act = knights()
msg = act("Robin")
print(msg)

# useful especially for jump tables

L = [lambda x: x**2,     # 3 functions embedded in a list!
     lambda x: x**3,
     lambda x: x**4]

for f in L:
    print(f(2))  # which returns 2^2, 2^3 and 2^4

print(L[2](3))  # prints 81, or 3^4; L[2] is x**4

# expressions can be placed in a single lambda
# example for selection logic, made easy

lower = (lambda x, y: x if x < y else y)
echo(lower(1, 10))  # calling funct echo to print, for fun

# nested lambdas:

action = (lambda x:(lambda y: x + y))
act = action(100)
echo(act(1))  # that's 100+1
