D = {'food': 'Chicken', 'quantity': 4, 'color': 'pink'}
# print(D['food']['quantity']) DOESN'T WORK
print(D['food'] + " now is " + str(D['quantity']))  # this one works fine instead
D['quantity'] += 1  # increase item quantity
print(D['food'] + " now is " + str(D['quantity']))
print("here is the full list with keys : {}".format(D))
print()

# Create keys by assignment
J = {'name': 'Bob', 'job': 'dev', 'age': 40}
print(J)
print(J['name'])

# Create dict with zipping
Z = dict(zip(['name', 'job', 'age'], ['Bob', 'dev', 40]))
print(Z)
print(Z['name'])

# Nested dictionary
rec = {'name': {'first': 'Bob', 'last': 'Smith'},
       'jobs': ['dev', 'mgr'],
       'age': 40.5}
print(rec)
print(rec['name']['last'] + ", " + rec['name']['first'])

print(rec['jobs'])
rec['jobs'].append("janitor")
print(rec['jobs'])
print(rec)

print("home" in rec)  # this is false since there's no home key in rec
if "home" not in rec:
    print("not there")
    print("sorry")
    print("no, really...")

# sorting the keys in a dictionary
Ks = list(rec.keys())
print(Ks)
Ks.sort()
print(Ks)
for key in Ks:
    print(key, "=>", rec[key], )
print()
# alternative to sorting is doing it directly in the if flow
for key in sorted(rec):
    print(key, "=>", rec[key])
