from ClassCreation_exercises import Person, Manager
import shelve

bob = Person("Mr.", "Bob Jones")
tom = Manager("Mr.", "Tom Malone", 50000)  # no need to specify job anymore
may = Person("Ms.", "May Jones", job="dev", pay=100000)

db = shelve.open("PersonDB")
for obj in (bob, tom, may):
    db[obj.name] = obj
# db.close() -> this command closes the db, I'll leave it open for now to play with it

print(len(db))
print(list(db.keys()))
bob = db["Bob Jones"]
print(bob)
print(bob.lastName())

for key in db:
    print(key, "->", db[key])

may = db["May Jones"]
may.giveRaise(.10)
db["May Jones"] = may  # update db value after raise
print(may)