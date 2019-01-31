# __author__ = "dev"
# greeting = "Bruce"
# _my_name = "Tim"
# Tim = "Good"
# Tim45 = "Good"
# Tim_was_57 = "Hello"
# Greeting = "There"
#
# # print(Tim_was_57 + " " + Greeting)
#
# a: int = 1
# b: int = 6
# print(a + b)  # è una expression
# print(a - b)
# print(a / b)
# print(a // b)
# print(a % b)
#
# for i in range(1, 14):
#     print(i + 1)
#
# Parrot = "Norwegian Blue"
# print(Parrot)
# print(Parrot[3])
# print(Parrot[0:8])
#
# numbers = "1, 2, 3, 4, 5, 6, 7, 8, 9"
# print(numbers[0::3])
#
# string1 = "he's "
# string2 = "probably"
# print(string1 + string2 + " gay")
#
# print("Hello" * 5)
#
# today = 'friday'
# print("day" in today)
# print("nigger" in today)
#
# age = 24
# print("My age is " + str(age) + " years")
#
# print("My age is {0} years".format(age))
#
# print("There are {0} days in {1}, {2}, {3}, ".format(31, "January", "March", "December"))
#
# print("My age is %d years" % age)
# print("My age is %d %s %d %s" % (age, "years", 6, "months"))
#
# for i in range(1, 12):
#     print("No. %2d squared is %4d and cubed is %4d" % (i, i ** 2, i ** 3))
#
# print("Pi is approximately %50.50f" % (22 / 7))
#
# for i in range(1, 19):
#     print("No. {0:<2} squared is {1:<4}and cubed is {2:<4}".format(i, i ** 2, i ** 3))
#
#     print("Pi is approximately {0:12.50}".format(22 / 7))


# x: int = input("Give me a number ")
# print (x + " is the selected number")
# for i in range(1, 14):
#     if int(x) >= 1:
#         print((x + str(i)) + " is the value you suggested before +" + str(i))
#     else:
#         print('Please give me a number that\'s higher than zero, thanks')
#
# import math
# x = 12
# if math.log(x, 2)>0:
#     print (str(math.log(x, 2)) + " wow what the hell did I just do")

#
# import math
# floor = math.floor(32.961651)
# print(floor)
#
# from math import sqrt
# print(sqrt(144))
#
# # Test program: Print a date given year, month and day as numbers
# months = ['January',
#           'February',
#           'March',
#           'April',
#           'May',
#           'June',
#           'July',
#           'August',
#           'September',
#           'October',
#           'November',
#           'December'
#           ]
# endings = ['st', 'nd', 'rd'] + 17 * ['th'] \
#           + ['st', 'nd', 'rd'] + 7 * ['th'] \
#           + ['st'] # first+second+third, then 4 to 20, then 21 to 23, then 24 to 30, then 31.
#
# year = input("Year: ")
# month = input("Month (1-12): ")
# day = input("Day (1-31): ")
#
# month_number = int(month)
# day_number = int(day)
#
# month_name = months[month_number - 1]  # the index starts from 0 so ì1 is needed!
# ordinal = day + endings[day_number - 1]  # same as before, index starts from 0.
#
# print(month_name[0:3] + ' ' + ordinal + ', ' + year)  #printed only 3 letters of the month, nice!
#
# for i in range (1, 12):
#     print("No. {} squared is {} and cubed is {:4}".format(i, i**2, i**4))
#     print("calculation complete")
#     print('try again')

# spam = {'name': 'Zophie', 'age': 7}
# print(spam["name"])
# print("name" in spam.keys())
# print("color" in spam.keys())

# list = {"name": "Alex", "age": 30}
# list.setdefault("color", "black")
# print(list)
# list("color", "yellow")
# print(list) #yellow doesn't get into the list since we already set the default as black earlier

import pprint

message = 'It was a bright cold day in April, and the clocks were striking thirteen'
count = {}
for character in message:
    count.setdefault(character, 0)
    count[character] = count[character] + 1

pprint.pprint(count)