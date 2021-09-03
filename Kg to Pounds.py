while True:
    operation = input("Would you like to do lbs to kg? Type: kg or Would you like kg to lbs? Type: lbs ")
    if operation == "kg":
        kg = float(input(" What is your weight in kg (Kilo Grams)?"))
        print (str(kg * 2.2) + " is your weight in pounds")

    elif operation == "lbs":
        lbs = float(input(" What is your weight in lbs (pounds)?"))
        print (str(lbs / 2.2) + " is your weight in kg (Kilo Grams)")

    else:
        print ("Please make sure it is all lower case and you follow the instructions!")

    again = input("Would you like to do another operation? yes or no? ")
    if again == "no":
        break