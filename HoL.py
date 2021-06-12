from random import randint

name = input("What is your name? ")

def hOL():
    secretNum = randint(1, 100)
    guess = eval(input("Guess a number between 1 and 100: "))
    while guess != secretNum:
       
        if guess > secretNum:
            print("Your guess was too big")
        else:
            print("Your guess was too small")
        guess = eval(input("Guess a number between 1 and 100: "))
    print("Congrats " + name + "!  You guessed the secret number!")
hOL()



    




