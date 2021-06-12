from random import randint

dice1 = str(randint(1, 6))
dice2 = str(randint(1, 6))
diceTotal = eval(str(dice1 + dice2))

def rolling(): 
    choice = input("1v1 or SP? ")
    if choice == "1v1":
        print("Player One Dice: " + dice1)
        print("Player Two Dice: "+ dice2)
        if dice1 > dice2:
            print("Player One Wins")
        if dice1 < dice2: 
            print("Player Two Wins")
        if dice1 == dice2:
            print("It's a tie!")
    else:
        print("Your dice are " + dice1 + " and " + dice2)
        print("Dice Total is " + diceTotal)


rolling()


