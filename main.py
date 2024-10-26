import functions as fun

tries = 0

def start_game():
    print("game")

def game():
    start_game()
    secuence = fun.duplicate_test(fun.create_value())
    win = False
    global tries
    while win == False:
        guess = fun.guess()
        if guess == secuence:
            print("Congratulations you win\n You did i in " + str(tries) + " tries")
            break
        else:
            bulls = fun.test_bull(secuence,guess)
            tries += 1
            cows = fun.test_cow(secuence, guess)
            print("The number of Bulls are " + str(bulls) + "\nThe number of Cows are " + str((cows-bulls)))

game()