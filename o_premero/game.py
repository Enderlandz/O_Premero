import random

def IsConvertibleToInt(number):
    for digit in number:
        if not digit.isdigit():
            return False
    return True

def getNumFromPlayer():
    ans = input('What is your guess?\n> ')
    while not IsConvertibleToInt(ans):
        print("I said a number. I'll be nice and not count this as an attempt")
        ans = input('Please input a valid guess\n> ')
    return int(ans)

def getValidInput():
    ans = getNumFromPlayer()
    while ans > 10:
        print("I said until 10! Since I'm nice, I won't count this attempt")
        ans = getNumFromPlayer()
    return ans

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
    print('Thanks for playing my game, {}!'.format(name))

    exit(0)
