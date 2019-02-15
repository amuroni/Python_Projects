class Worker:
    def __init__(self, name, pay):  # defining the main class attributes, self is the subject of the class!
        self.name = name  # attribute aka "state information"
        self.pay = pay  # attribute aka "state information"
    def lastName(self):
        return self.name.split()[-1]  # splits the string on blanks!
    def giveRaise(self, percent):
        self.pay *= (1.0 + percent)  # update on pay raise


bob = Worker('Bob Smith', 50000)  # Make two instances
sue = Worker('Sue Jones', 60000)  # Each has name and pay attributes

print(bob.lastName())  # call the method were "bob" is "self"
print(sue.lastName())
print(str(sue.pay) + " € before the raise")
sue.giveRaise(.10)
print(str(round(sue.pay)) + " € after the raise, nice!") # rounded the number too
print("***********")

class rec: pass

pers1 = rec()
pers1.name = "Bob"
pers1.job = ["dev", "manager"]
pers1.age = 30

print("My name is", pers1.name + ", I'm a", str(pers1.age) + " years old", pers1.job[0])

