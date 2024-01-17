import random

word_list = ['cactus', 'strawberry', 'peach', 'pear', 'watermelon']
word = random.choice(word_list)

print(word)

guess = input("enter a letter: ")

if len(guess) == 1 and guess.isalpha():
    print("Good guess!")
else: print("Oops! That is not a valid input.")