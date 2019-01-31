# # This is a guess the number game.
# import random
# secretNumber = random.randint(1, 20)
# print('I am thinking of a number between 1 and 20.')
#
# for guessesTaken in range(1, 7):
#     print('Take a guess.')
#     guess = int(input())
#
#     if guess < secretNumber:
#         print('Your guess is too low.')
#     elif guess > secretNumber:
#         print('Your guess is too high.')
#     else:
#         break # This condition is the correct guess!
# if guess == secretNumber:
#     print('Good job! You guessed my number in ' + str(guessesTaken) + ' guesses!')
# else:
#     print('Nope. The number I was thinking of was ' + str(secretNumber))

import random

messages = ['It is certain',
            'It is decidedly so',
            'Yes definitely',
            'Reply hazy try again',
            'Ask again later',
            'Concentrate and ask again',
            'My reply is no',
            'Outlook not so good',
            'Very doubtful'
            'How about NO']

print(messages[random.randint(0, len(messages) - 1)])  # value between 0 and the length of messages -1