from random import randint
playerCard1 = randint(1, 10)
playerCard2 = randint(1, 10)

def Game(): 
    hand = playerCard1 + playerCard2
    print("Hand is equal to " + str(hand))
    while hand < 21:
        choice = input("Hit or Stand?")
        if choice == "Hit": 
            hand + randint(1, 10)
            print(str(hand))
        if choice == "Stand":
            print("Your hand is "  + str(hand))
Game()








