import random
import os

WORDS = ["handkerchief", "accommodate", "indict", "impetuous","exponentially","incredible","apothecary", "taxidermist","oceanography","intelligence"]
MAX_GUESSES = 7



print("^^^^^^^^^^THIS IS HANGMAN^^^^^^^^^^")

while True:

    input('Press <ENTER> to start a new game or <CTRL>+<C> to quit.')

    word = random.choice(WORDS)
    guess = ['_'] * len(word)
    guesses = set()
    n = MAX_GUESSES

    while True:

        print('\nYour word:', ' '.join(guess))
        print('You have {} chances left.'.format(n))

        if '_' not in guess:
            print('Congratulations, you win!\n')
            break

        if n < 1:
            print('Sorry, no guesses left. You lose!\n')
            break

        character = input('Guess a new character: ')

        if len(character) != 1:
            print('You must enter exactly one character!')


        if character in guesses:
            print('You have already guessed that character!')


        guesses.add(character)

        if character not in word:
            n -= 1


        for i, c in enumerate(word):
            if c == character:
                guess[i] = character

        
