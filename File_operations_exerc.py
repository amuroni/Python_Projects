# f = open("data.txt", "w")  # makes a new file in output mode, since w means "Write""
# f.write("hello\n")
# f.write("world\n")
# f.close()

f = open("data.txt")
text = f.read()  # reads the content of the "data.txt" file which is now assigned to variable f via f = ____
print(text.split())

for line in open("data.txt"):
    print(line)
