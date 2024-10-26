import random

def duplicate_test(num):
    temp = []
    for x in num:
        if str(x) in temp:
            return duplicate_test(create_value())
        else:
            temp.append(str(x))
    return temp

def create_value():
    value = []
    count = 4
    while count > 0:
        value.append(random.randint(0,9))
        count -=1
    return value

def guess():
    try:
        gues = input ("Make a four number guess ")
        guessL = list(gues)
        return guessL
    except ValueError: return ("Please enter only numbers")

def check_guess(gues):
    if len(gues) != 4: return ("It has to be a guess of 4 numbers")
    else: return gues

def test_bull(number, guess):
    bull = 0
    for element in enumerate(number):
        if element in enumerate(guess):
            bull += 1
    return bull

def test_cow(guess, num):
    cow = 0
    for index in guess:
        if index in num:
            cow += 1
        else: None
    return cow