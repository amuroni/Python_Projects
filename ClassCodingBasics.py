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
print(rec2.info())

"""
main classes ides:
INHERITANCE : attribute lookup (i.e. in x.name expressions etc) 
POLYMORPHISM: in x.method the meaning of method depends on the type/class of obj x
ENCAPSULATION: methods and operators implement behavior + data hiding by default 
"""
