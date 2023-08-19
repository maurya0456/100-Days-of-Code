print("Welcome to Treasure island, Your mission is to find the treasure")

choice1 = input("Which side do you wanna go? lift or right? Choice is yours").lower()

if choice1 == 'left':
    print("You have reached to the port")
    choice2 = input("What do you want to do? swim or wait? Choice is yours").lower()
    if choice2 == 'wait':
        print("You have to final destination, you just have to pass the final test, so ahead")
        choice3 = input("Which color gate do you wanna go? Red, Yellow or Blue? Choice is yours").lower()
        if choice3 == 'yellow':
            print("You WIN!!!!!")
        else:
            print("Game OVER, You LOSE!!!")
    else:
        print("Crocodile is very dangerous, Wrong choice, you are dead now, GAME OVER")
else:
    print("Go to Hell, HAHAHAHAHA")
