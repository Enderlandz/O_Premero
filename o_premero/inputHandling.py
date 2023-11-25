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