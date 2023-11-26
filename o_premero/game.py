import random

from o_premero.inputHandling import getValidInput

def entry():
    num = random.randint(0, 10)
    tries = 0
    maxTries = 3
    name = input('What is your name?\n> ')
    gameIsRunning = True
    print('Hello, {}.'.format(name))
    print('I am thinking of a number between 0 and 10')
    print('Try guessing the number in {} tries!'.format(maxTries))
    while gameIsRunning:
        tries = tries + 1
        ans = getValidInput()
        remainingTries = maxTries - tries
        if tries == maxTries:
            gameIsRunning = False
        if ans < 0:
            print('Not valid!')
        if ans < num:
            print('A little higher, {} tries left'.format(remainingTries))
        if ans > num:
            print('A little lower, {} tries left'.format(remainingTries))
        if ans == num:
            print('You got it!')
            gameIsRunning = False
    print('The number was {}'.format(num))
    print('Thanks for playing my game, {}!'.format(name))

    exit(0)
