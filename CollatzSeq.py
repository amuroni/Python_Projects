# number = int(input("Please input a number "))
#
# def collatz(number):
#     if (number % 2 == 0):
#         new_number = number // 2
#         print(new_number)
#         if new_number != 1:
#             collatz(new_number)
#         else:
#             return new_number
#     elif (number % 2 == 1):
#         new_number = number * 3 + 1
#         print(new_number)
#         collatz(new_number)
#


def user_input():
    number = int(input("Please input a positive integer (at least 2): "))
    if number in [0, 1, 2] or number < 0:
        print("A positive number at least equal to 2, please!")
    else:
        collatz(number)


def collatz(n):
    if n == 1:
        return "The value is 1"
    else:
        new_number = n // 2 if n % 2 == 0 else n * 3 + 1
        print(new_number)
        collatz(new_number)

number = user_input()
