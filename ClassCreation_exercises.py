class Worker:
    def __init__(self, name, pay):  # defining the main class attributes, self is the subject of the class!
        self.name = name  # attribute aka "state information"
        self.pay = pay  # attribute aka "state information"

    def lastname(self):
        return self.name.split()[-1]  # splits the string on blanks!

    def giveraise(self, percent):
        self.pay *= (1.0 + percent)  # update on pay raise


bob = Worker('Bob Smith', 50000)  # Make two instances
sue = Worker('Sue Jones', 60000)  # Each has name and pay attributes

print(bob.lastname())  # call the method were "bob" is "self"
print(sue.lastname())
print(str(sue.pay) + " € before the raise")
sue.giveraise(.10)
print(str(round(sue.pay)) + " € after the raise, nice!") # rounded the number too
print("***********")


class rec: pass


pers1 = rec()
pers1.name = "Bob"
pers1.job = ["dev", "manager"]
pers1.age = 30

print("My name is", pers1.name + ", I'm a", str(pers1.age) + " years old", pers1.job[0])


class Person:
    def __init__(self, gender, name, job=None, pay=0):  # class with default args
        self.gender = gender                            # added a gender attribute
        self.name = name
        self.job = job
        self.pay = pay

    def lastname(self):                         # add specific methods to encapsulate operations
        return self.name.split()[-1]

    def giveraise(self, percent):
        self.pay = int(self.pay * (1 + percent))

    def __repr__(self):
        return "[Person: %s %s, Salary: %s Euro]" % (self.gender, self.name, self.pay)  # method and print + % format


class Manager(Person):  # this one is a subclass of person! inherits person attrs
    def __init__(self, gender, name, pay):
        Person.__init__(self, gender, name, "mgr", pay)  # job =mgr by subclass default

    def giveraise(self, percent, bonus=.10):
        Person.giveraise(self, percent + bonus)  # augmented the original giveraise def


if __name__ == "__main__":
    tom = Manager("Mr.", "Tom Malone", 50000)  # no need to specify job anymore
    may = Person("Ms.", "May Jones", job="dev", pay=100000)
    print("All persons")
    for obj in (tom, may):
        obj.giveraise(.10)
        print(obj)

# instead of using the code below, we process all obj at one
# print("My name is", may.name, "and my pay is", may.pay, "Euro")
# print(may.lastname())
# # may.giveraise(.30)
# print(may.pay)
# print(may)     # reminder: may is an object! with __repr__ we print directly self.name and self.pay
#
# # tom.giveraise(.10)  # customized giveraise with 0.10 + 0.10 = 0.20 total.
# print(tom.lastname())
# print(tom)

