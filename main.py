import random

lives = 3
print("Welcome to the maze door game!")
print("You will go through many sets of doors in hopes of getting to the treasure at the end")

while lives != 0:
    correct_door = random.randint(1, 2)

    set1 = int(input("Choose the first door: "))
    if set1 != correct_door:
        print("Sorry, you did not choose the first correct door.")
        lives -= 1
        print(str(lives))
    elif set1 == correct_door:
        print("Congratulations! You made it through the first door.")
        if lives == 0:


            set2 = int(input("Choose the second door: "))
            if set2 == correct_door:
                print("Congratulations! You made it through the second door.")
            elif set2 != correct_door:
                print("Sorry, you did not choose the second correct door.")
                lives -= 1
                print(str(lives))
                if lives == 0:
                    break