import random


def getanswer(answernumber):
    if answernumber == 1:
        return "It is certain"
    elif answernumber == 2:
        return "It is decidedly so"
    elif answernumber == 3:
        return "Yes"
    elif answernumber == 4:
        return "Maybe"
    elif answernumber == 5:
        return "No"
    elif answernumber == 6:
        return "Definitely NO!"


# r = random.randint(1, 3)
# fortune = getanswer(r)
# print(fortune)

print(getanswer(random.randint(1, 6)))