alphabet = ["a", "b", "c", "d", "e", "", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
vowels = ["a", "e", "i", "o", "u"]

for i in range(len(alphabet)):  # max length is alphabet, if you put vowels it goes out of nums
    if alphabet[i] in vowels:  # no need to check vowels[i] - it compares the alphabet[i] with the whole vowels list!
        print(alphabet[i] + " is a vowel, nice!")
    # else:
    #     # print(alphabet[i] + " is not a vowel!")
    #     pass  # instead if printing not vowels, better passing it
# or even better, put no else condition and just print the vowels, right?
