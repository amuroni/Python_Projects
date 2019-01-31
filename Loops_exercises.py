for i in range(3):
    print(i, "Python")

X = 'SPAM'
for item in X:
    print(item, end='.')
print()
i = 0
while i < len(X):
    print(X[i], end=" ")
    i += 1
print()
S = 'spam'
for i in range(len(S)):  # For repeat counts 0123
    S = S[1:] + S[:1]  # Moves front item to end
    print(S, end=' ')

L1 = [1, 2, 3, 4]
L2 = [5, 6, 7, 8]

merged = zip(L1, L2)  # this merges the lists L1 and L2 together
print(list(merged))

for (x, y) in zip(L1, L2):  # for some reason using merged does not work, maybe because of parameters missing
    print(x, "+", y, "->", x+y)

T1, T2, T3, = (1, 2, 3,), (4, 5, 6), (7, 8, 9)
print(T3)
print()
T = T1 + T2 + T3
print(T)
print(list(zip(T1, T2, T3)))

for i in range(0, 3):
    x = (T1[i] + T2[i] + T3[i])
    print(x)
print()

y = int
for i in range(len(T)):
    y = (T[i]) + y
    print(y)
print()

keys = ['spam', 'eggs', 'toast']
vals = [1, 3, 5]
# join this two lists with zip
ziplist = list(zip(keys, vals))
print(ziplist)
