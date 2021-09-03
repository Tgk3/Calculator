import random

lives = 7
print("Welcome to the maze door game!")
print("You will go through many sets of doors in hopes of getting to the treasure at the end")

def lostlives():
    global lives
    lives -= 1
    print(str(lives), "are your lives remaining")

def again():
    again = input("Would you like to play again? 'yes' for YES or 'no' for NO: ")
    if again == "yes":
        global lives
        lives += 7

    else:
        print("Thank you for playing!")
        lives = 0


while lives != 0:
#Set 1
    set1 = int(input("Choose the first door: "))
    correct_door1 = random.randint(1, 3)
    if set1 != correct_door1:
        print("Sorry, you did not choose the first correct door.")
        lostlives()

        if lives == 0:
            again()

    elif set1 == correct_door1:
        print("Congratulations! You made it through the first door.")

#Set 2
        set2 = int(input("Choose the second door: "))
        correct_door2 = random.randint(1, 3)
        if set2 != correct_door2:
            print("Sorry, you did not choose the second correct door.")
            lostlives()

            if lives == 0:
                again()

        if set2 == correct_door2:
            print("Congratulations! You made it through the second door.")

 #Set 3
            set3 = int(input("Choose the third door: "))
            correct_door3 = random.randint(1, 3)
            if set3 != correct_door3:
                print("Sorry, you did not choose the third correct door.")
                lostlives()

                if lives == 0:
                    again()

            elif set3 == correct_door3:
                print("Congratulations! You made it through the third door.")
                print("You did it! You won the game...Were you expecting a cookie or something?")
                again()