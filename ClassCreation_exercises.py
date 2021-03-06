# class Worker:
#     def __init__.py(self, name, pay):  # defining the main class attributes, self is the subject of the class!
#         self.name = name  # attribute aka "state information"
#         self.pay = pay  # attribute aka "state information"
#
#     def lastname(self):
#         return self.name.split()[-1]  # splits the string on blanks!
#
#     def giveraise(self, percent):
#         self.pay *= (1.0 + percent)  # update on pay raise
#
#
# bob = Worker('Bob Smith', 50000)  # Make two instances
# sue = Worker('Sue Jones', 60000)  # Each has name and pay attributes
#
# print(bob.lastname())  # call the method were "bob" is "self"
# print(sue.lastname())
# print(str(sue.pay) + " € before the raise")
# sue.giveraise(.10)
# print(str(round(sue.pay)) + " € after the raise, nice!") # rounded the number too
# print("***********")
#
#
# class rec: pass  # class with no defs inside, assigned below
#
#
# pers1 = rec()
# pers1.name = "Bob"
# pers1.job = ["dev", "manager"]
# pers1.age = 30
#
# print("My name is", pers1.name + ", I'm a", str(pers1.age) + " years old", pers1.job[0])



# class Person:
#     def __init__.py(self, gender, name, job=None, pay=0):  # class with default args
#         self.gender = gender                            # added a gender attribute
#         self.name = name
#         self.job = job
#         self.pay = pay
#
#     def lastname(self):                         # add specific methods to encapsulate operations
#         return self.name.split()[-1]
#
#     def giveraise(self, percent):
#         self.pay = int(self.pay * (1 + percent))
#
#     def __repr__(self):
#         return "[Person: %s %s, Job: %s, Salary: %s Euro]" % (self.gender, self.name, self.job, self.pay)  # method and print + % format
#
#
# class Manager:  # this one is a subclass of person! inherits person attrs; uses class delegation
#     def __init__.py(self, gender, name, pay):
#         self.person = Person(gender, name, "mgr", pay)  # job =mgr by subclass default + embed person obj
#
#     def giveraise(self, percent, bonus=.10):
#         self.person.giveraise(percent + bonus)  # intercept person giveraise, use percent + bonus
#
#     def __getattr__(self, attr):
#         return getattr(self.person, attr)       # delegate other attributes
#
#     def __repr__(self):
#         return str(self.person)


# class Department:  # = aggregating embedded objs into a composite obj
#     def __init__.py(self, *args):
#         self.members = list(args)
#
#     def addmember(self, person):
#         self.members.append(person)
#
#     def giveraises(self, percent):
#         for person in self.members:
#             person.giveraise(percent)
#
#     def showall(self):
#         for person in self.members:
#             print(person)


# if __name__ == "__main__":
#     bob = Person("Mr.", "Bob Jones", "dev", 20000)
#     tom = Manager("Mr.", "Tom Malone", 50000)  # no need to specify job anymore
#     may = Person("Ms.", "May Jones", job="dev", pay=100000)
    # print("All persons")
    # for obj in (tom, may):
    #     obj.giveraise(.10)
    #     print(obj)
#
# development = Department(bob, may)  # development = name of aggregate obj Department
# development.addmember(tom)
# development.giveraises(.10)
# development.showall()
#
# # instead of using the code below, we process all objs at one
# # print("My name is", may.name, "and my pay is", may.pay, "Euro")
# # print(may.lastname())
# # # may.giveraise(.30)
# # print(may.pay)
# # print(may)     # reminder: may is an object! with __repr__ we print directly self.name and self.pay
# #
# # # tom.giveraise(.10)  # customized giveraise with 0.10 + 0.10 = 0.20 total.
# # print(tom.lastname())
# # print(tom)
#
# print(bob.__class__.__name__)  # = Person
# for key in bob.__dict__:
#     print(key, "->", bob.__dict__[key])  # returns all keys in bob's Person dict
# # or
# for key in bob.__dict__:
#     print(key, "->", getattr(bob, key))

from Classtools import AttrDisplay


class Person(AttrDisplay):  # better use of attrdisplay to define Person class
    def __init__(self, gender, name, job=None, pay=0):
        self.gender = gender
        self.name = name
        self.job = job
        self.pay = pay

    def lastName(self):
        return self.name.split()[-1]

    def giveRaise(self, percent):
        self.pay = int(self.pay * (1 + percent))


class Manager(Person):
    def __init__(self, gender, name, pay):
        Person.__init__(self, gender, name, "mgr", pay)

    def giveraise(self, percent, bonus=.10):
        Person.giveRaise(self, percent + bonus)


if __name__ == "__main__":
    bob = Person("Mr.", "Bob Jones")
    tom = Manager("Mr.", "Tom Malone", 50000)  # no need to specify job anymore
    may = Person("Ms.", "May Jones", job="dev", pay=100000)
    print(bob)
    print(tom)
    print(may)
    print(bob.lastName(), tom.lastName())
    may.giveRaise(.10)
    tom.giveRaise(.10)
    print(may.pay)
    print(tom.pay)