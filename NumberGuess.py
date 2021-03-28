Number = int(input ("Please enter a number between 1 and 10 here:   "))
Number1 = 0
if (Number>5):
    Number1=Number -4

if (Number<5):
    Number1=Number + 4

Guess1 = int(input("Please guess the generated number:   "))
if (Guess1==Number1):
    print("Wow, You Did It !!")

if (Guess1 != Number1):
    print ("Uh oh, Try Again :(")
    Guess2 = int(input("Please guess the generated number:   "))
    if (Guess2==Number1):
        print("Wow, You Did It !!")
    if (Guess2 != Number1):
        print ("Uh oh, Try Again :( (Last Chance Left)")
        Guess3 = int(input("Please guess the generated number:   "))
        if (Guess3==Number1):
            print("Wow, You Did It !!")
        if (Guess3 != Number1):
            print ("Uh oh, You Ran Out of Tries, the number was:")
            print (Number1)


