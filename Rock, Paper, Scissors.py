from random import randint

#Creating a list of options
options = ["rock", "paper", "scissors"]

#assign a random play to the computer
computer = options[randint(0,2)]

#set player to false



while True:

    player = input("Choose between rock, paper, scissors ")

    if player == computer:
        print ("It's a Tie! ")

    elif player == "rock":
        if computer == "paper":
            print ("You lose ", computer, "covers ", player)
        elif computer == "scissors":
            print ("You win! ",player, "breaks ", computer)

    elif player == "paper":
        if computer == "scissors":
            print ("You lose ", computer, "cuts ", player)
        elif computer == "rock":
            print ("You Win! ", player, "breaks", computer)

    elif player == "scissors":
        if computer == "rock":
            print ("You lose ", computer, "breaks ", player)
        elif computer == "paper":
            print ("You Win! ", player, "cuts ", computer)

    else:
        print("Sorry it has to be all lowercase and no spaces! ")
