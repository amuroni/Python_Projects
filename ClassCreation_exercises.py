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
print(str(round(sue.pay)) + " € after the raise, nice!")
# WELL NICE JOB MAN, nice job, I automatically rounded the number myself with no instructions, just by guessing. NICE
