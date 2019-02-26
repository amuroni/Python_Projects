from __future__ import print_function                                       # should be at the top

"""
classes generate multiple instance objects:
with class statements, a class obj is created and a name assigned to it
assignments inside the class are attributes, which provide obj state and behavior
calling a class makes a new instance object
"""

class FirstClass:
    def setdata(self, value):
        self.data = value
    def display(self):
        print(self.data)


x = FirstClass()
y = FirstClass()

x.setdata("King")
y.setdata("16/11/1988")
x.display()
y.display()

"""
classes are customized by INHERITANCE
the subclass must reference the superclass in ()
classes INHERIT attrs from their superclasses
instances inherit attrs from all accessible classes
each object.attribute ref invokes a new independent search
logic changes are mad on a subclass level, not by changing the superclass!
"""


class SecondClass(FirstClass):
    def display(self):                           # overrides the FirstClass method
        print("Current value = %s" % self.data)


z = SecondClass()
z.setdata(42)
z.display()

"""
methods with underscores __x__ are class constructors, called automatically in built-in operations, ex. __add__ = +
__init__ run when new instance of obj is created;
__add__ run when a + expression is used
__str__ run when an obj is printed or converted to its print string by str function
etc..
"""


class ThirdClass(SecondClass):       # instances are inherited from secondclass
    def __init__(self, value):
        self.data = value

    def __add__(self, other):
        return ThirdClass(self.data + other)

    def __str__(self):
        return "[Thirdclass: %s]" % self.data

    def mul(self, other):
        self.data *= other


a = ThirdClass("abc")
a.display()
print(a)
b = a + "xyz"
b.display()
print(b)
a.mul(3)
print(a)


class Rec:
    pass  # = empty namespace object


Rec.name = "Bob"  # assign objects and attributes
Rec.age = 40
Rec.jobs = ["dev", "mgr"]

print(Rec.name)

x = Rec()  # instances inherit previous class names
y = Rec()

print(x.name, y.name)  # still Bob, name stored in class

x.name = "Sue"  # only affects x!
print(Rec.name, x.name, y.name)  # x is now Sue, y is still Bob

pers1 = Rec()
pers1.name = "Bob"
pers1.jobs ="dev"
pers1.age = 40.5

pers2 = Rec()
pers2.name = "Joe"
pers2.jobs = "Mgr"
pers2.age = 42

# better done by creating a specific Person class:

class Person:

    def __init__(self, name, jobs, age=None):
        self.name = name
        self.jobs = jobs
        self.age = age

    def info(self):
        return self.name, self.jobs, self.age if self.age is not None else "Age not defined"


rec1 = Person("Bob", "Dev", 42)
rec2 = Person("Joe", "Mgr")
print(rec1.info())
print(rec2.info()); print()

"""
main classes ides:
INHERITANCE : attribute lookup (i.e. in x.name expressions etc) 
POLYMORPHISM: in x.method the meaning of method depends on the type/class of obj x
ENCAPSULATION: methods and operators implement behavior + data hiding by default 
"""


class Employee:                                                             # main class
    def __init__(self, name, salary=0):
        self.name = name
        self.salary = salary

    def giveRaise(self, percent):
        self.salary = self.salary + (self.salary * percent)

    def work(self):
        print(self.name, "does stuff")

    def __repr__(self):
        return "<Employee: name=%s, salary=%s>" % (self.name, self.salary)


class Chef(Employee):                                                       # chef subclass
    def __init__(self, name):
        Employee.__init__(self, name, 50000)                                # inherit employee attrs

    def work(self):
        print(self.name, "makes food")


class Server(Employee):                                                     # server subclass
    def __init__(self, name):
        Employee.__init__(self, name, 40000)

    def work(self):
        print(self.name, "interfaces with customer")


class PizzaRobot(Chef):                                                     # robot subclass
    def __init__(self, name):
        Chef.__init__(self, name)

    def work(self):
        print(self.name, "makes pizza")


if __name__ == "__main__":
    bob = PizzaRobot("bob")                          # create the robot
    print(bob)                                       # base salary 40k
    bob.work()                                       # print job
    bob.giveRaise(0.2)                               # raise +20% - inherits giveRaise method from employee
    print(bob); print()

    for klass in Employee, Chef, Server, PizzaRobot:  # print all classes name + job
        obj = klass(klass.__name__)
        obj.work()
print("****")


class Customer:                                       # create customer class
    def __init__(self, name):
        self.name = name

    def order(self, server):
        print(self.name, "orders from", server)

    def pay(self, server):
        print(self.name, "pays for item to", server)


class Oven:
    def bake(self):
        print("oven bakes")


class PizzaShop:                                             # contains employees & oven classes
    def __init__(self):
        self.server = Server('Pat')                          # Embed other objects
        self.chef = PizzaRobot('Bob')                        # A robot named bob
        self.oven = Oven()

    def order(self, name):
        customer = Customer(name)                            # Activate other objects
        customer.order(self.server)                          # Customer orders from server
        self.chef.work()                                     # Chef makes pizza
        self.oven.bake()                                     # Oven bakes pizza
        customer.pay(self.server)                            # Customer pays pizza


if __name__ == "__main__":
    scene = PizzaShop()
    scene.order("Homer")
    print("****")
    scene.order("Shaggy")

print("******")


class Processor:
    def __init__(self, reader, writer):
        self.reader = reader
        self.writer = writer

    def process(self):
        while True:
            data = self.reader.readline()
            if not data: break
            data = self.converter(data)
            self.writer.write(data)

    def converter(self, data):
        assert False, "converter must be defined"


class Uppercase(Processor):
    def converter(self, data):
        return data.upper()


if __name__ == "__main__":
    import sys
    obj = Uppercase(open("data.txt"), sys.stdout)
    obj.process()

print("****")


class Wrapper:
    def __init__(self, object):
        self.wrapped = object                   # save obj

    def __getattr__(self, attrname):
        print("Trace: " + attrname)             # trace fetch
        return getattr(self.wrapped, attrname)  # delegate fetch to getattr function


x = Wrapper([1, 2, 3])
print(x.wrapped)
x.append(4)
print(x.wrapped); print("****")


class Selfless:
    def __init__(self, data):
        self.data = data

    def selfless(arg1, arg2):
        return arg1 + arg2

    def normal(self, arg1, arg2):         # expects an instance when called
        return self.data + arg1 + arg2


X = Selfless(2)

print(X.normal(3, 4))            # passed to self automatically, so 2+3+4 = 9
print(Selfless.normal(X, 3, 4))  # self expected by method, so auto pass: = 9
print(Selfless.selfless(3, 4))   # no X instance: result = 7
# Selfless.normal(3, 4)          Error: missing 1 pos arg - expected an X instance
# X.selfless(3, 4)               Error: 2 pos args but 3 were given - does not expect the X instance

# bound methods and other callable objs


class Number:
    def __init__(self, base):
        self.base = base

    def double(self):
        return self.base * 2

    def triple(self):
        return self.base * 3


x = Number(2)
y = Number(3)
z = Number(4)
x.double()   # returns 4, like a normal call

acts = [x.double, y.double, y.triple, x.triple, z.double]  # list of bound methods
for act in acts:                                           # deferred calls for each obj
    print(act())                                           # call as func


def square(arg):
    return arg ** 2


class Sum:
    def __init__(self, val):
        self.val = val

    def __call__(self, arg):
        return self.val + arg


class Product:
    def __init__(self, val):
        self.val = val

    def method(self, arg):
        return self.val * arg


class Negate:
    def __init__(self, val):
        self.val = -val

    def __repr__(self):
        return str(self.val)


print("*****")

s_obj = Sum(2)
p_obj = Product(3)

actions = [square, s_obj, p_obj.method]
for act in actions:
    print(act(5))

print(actions[+1](5))  # still 15, or p_obj on num 3 -> 5*3
print([act(5) for act in actions])  # [25, 7, 15]
print(list(map(lambda act: act(5), actions)))  # [25, 7, 15]

actions = [square, s_obj, p_obj.method, Negate]  # also with Negate class
for act in actions:
    print(act(2))
