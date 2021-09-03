while True:
    operation = (input("Choose a type of operation: For multiplication type m , For addition type a"
                        ", For subtraction type s, For division type d "))
    number_1 = float(input("Choose the first number for your operation "))
    number_2 = float(input("Choose the second number for your operation "))
    if operation == "m":
        print(number_1 * number_2)

    elif operation == "a":
        print(number_1 + number_2)

    elif operation == "s":
        print(number_1 - number_2)

    elif operation == "d":
        print(number_1 / number_2)

    else:
        print("Sorry I'm not smart enough :( ")

    again = (input("Would you like to do another operation? yes or no? "))
    if again == "no":
        print("Thank you for using me Good Bye!")
        break
