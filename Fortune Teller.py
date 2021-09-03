print ("Welcome to the fortune teller game ")
print ("You will pick a colour and a number and your future shall be foretold")
while True:
    user_answer = (input("Pick a colour: red, blue, green, yellow "))
    if user_answer == "red" or user_answer == "blue":
        user_answer2 = (int(input("Pick a number: 3,4,7,8 ")))
        if user_answer2 == 3:
            print("You will stumble upon a broken watermelon")
        elif user_answer2 == 4:
            print("You should perform an act of charity it will come back")
        elif user_answer2 == 7:
            print("Carry an umbrella tomorrow")
        elif user_answer2 == 8:
            print("You will stumble upon gold")
        else:
            print("You probably think Santa Claus exists...stupid")


    elif user_answer == "green" or user_answer == "yellow":
        user_answer2 = (int(input("Pick a number: 1,2,5,6 ")))
        if user_answer2 == 1:
            print("You will become famous and popular world wide")
        elif user_answer2 == 2:
            print("You will be healthy and a fit person...if you workout fatass")
        elif user_answer2 == 5:
            print("You will travel the world...or at least you think but you just ate some shrooms")
        elif user_answer2 == 6:
            print("All your dreams will come true...while you are sleeping")
        else:
            print("You probably think Santa Claus exists...stupid")

    else:
        print("You have to pick one of the 4 colours, make sure it is all lower-case")

    again = (input("Do you want to play again? Type y or n "))
    if again == "n":
        break