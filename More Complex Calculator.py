while True:
    operation = (input("Choose a type of operation: For multiplication type m , For addition type a"
                        ", For subtraction type s, For division type d "))
    number_1 = float(input("Choose the first number for your operation "))
    number_2 = float(input("Choose the second number for your operation "))
    m = (number_1 * number_2)
    a = (number_1 + number_2)
    s = (number_1 - number_2)
    d = (number_1 / number_2)
    if operation == "m":
        print (str(number_1) + (" * ") + (str(number_2) + (" = ") + (str(m))))

    elif operation == "a":
        print(str(number_1) + (" + ") + (str(number_2) + (" = ") + (str(a))))

    elif operation == "s":
        print (str(number_1) + (" - ") + (str(number_2) + (" = ") + (str(s))))

    elif operation == "d":
        print (str(number_1) + (" / ") + (str(number_2) + (" = ") + (str(d))))

    else:
        print("Sorry I'm not smart enough :( ")

    again = (input("Would you like to do another operation? yes or no? "))
    if again == "no":
        print("Thank you for using me Good Bye!")
        break