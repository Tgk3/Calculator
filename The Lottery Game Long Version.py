while True:
    from random import randint

    options = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
    lottery = options[randint(0, 9)]
    print("Hello! Welcome To The Lottery Game! ")
    print("You will have 5 attempts guess the right number between 1 and 10! ")

    #Choose Your Name
    name = input("What is your name? ")
#Choose First Number
    first_number = input("Choose The First Number! ")
    if first_number == lottery:
        print("Congratulations ", name, "you got it on the first attempt ")

        again = input("Do you want to play again? yes or no ")
        if again == "no":
            print("Thank you for playing")
            break

    elif first_number < lottery:
        print ("Sorry", name, "Too Low Try Again! ")

    elif first_number > lottery:
        print ("Sorry", name, "Too High Try Again! ")

    else:
        print("Sorry it has to be a number between 1 and 10 ")


#Choose Second Number
    second_number = input("Choose The Second Number! ")
    if second_number == lottery:
        print("Congratulations ", name, "you got it on the second attempt ")

        again = input("Do you want to play again? yes or no ")
        if again == "no":
            print("Thank you for playing")
            break

    elif second_number < lottery:
        print("Sorry", name, "Too Low Try Again! ")

    elif second_number > lottery:
        print("Sorry", name, "Too High Try Again! ")

    else:
        print("Sorry it has to be a number between 1 and 10 ")

#Choose Third Number
    third_number = input("Choose The Third Number! ")
    if third_number == lottery:
        print("Congratulations ", name, "you got it on the third attempt, ")

        again = input("Do you want to play again? yes or no ")
        if again == "no":
            print("Thank you for playing")
            break

    elif third_number < lottery:
        print("Sorry", name, "Too Low Try Again! ")

    elif third_number > lottery:
        print("Sorry", name, "Too High Try Again! ")

    else:
        print("Sorry it has to be a number between 1 and 10 ")

#Choose Fourth Number
    fourth_number = input("Choose The Fourth Number! ")
    if fourth_number == lottery:
        print("Congratulations ", name, "you got it on the fourth attempt ")

        again = input("Do you want to play again? yes or no ")
        if again == "no":
            print("Thank you for playing")
            break

    elif fourth_number < lottery:
        print("Sorry", name, "Too Low Try Again! ")

    elif fourth_number > lottery:
        print("Sorry", name, "Too High Try Again! ")

    else:
        print("Sorry it has to be a number between 1 and 10 ")
#Choose Fifth Number
    fifth_number = input("Choose The Fifth Number! ")
    if fifth_number == lottery:
        print("Congratulations ", name, "you got it on the fifth attempt ")

        again = input("Do you want to play again? yes or no ")
        if again == "no":
            print("Thank you for playing")
            break

    elif fifth_number < lottery:
        print("Sorry", name, "You ran out of Tries! ")

    elif fifth_number > lottery:
        print("Sorry", name, "Sorry you ran out of Tries! ")