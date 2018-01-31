from random import *

print("Welcome to the Number Reduction Game!")
print("You will be playing against a computer.")
print("")

order = input("Would you like to go first? (Y/N): ")
print("")

if order in ["Y", "y"]:
    num = int(input("Enter a starting number: "))
    
else:
    print("The computer will choose a starting number.")
    num = randint(10, 100)
    print("The computer chose", num)
    print("")

    C1 = num - 1 
    C2 = int(num/2)
    playerChoice = int(input("Your choices are " + str(C1) + " or " + str(C2) + ": "))

    while playerChoice not in [C1, C2]:
        print("That is not an option. Try again.")
        print("")
        playerChoice = int(input("Your choices are " + str(C1) + " or " + str(C2) + ": "))

    num = playerChoice
    print("You chose", num)

print("")

while num > 0:
    
    C1 = num - 1 
    C2 = int(num/2)
    if C1 == C2:
        print("The computer's only choice is", C1)
        num = C1
    else: 
        print("The computer's choices are", C1, "or", C2)
        if C1 % 2 == 0 and C2 % 2 != 0:
            num = C1
        elif C1 % 2 != 0 and C2 % 2 == 0:
            num = C2
        elif C1 % 2 == 0 and C2 % 2 == 0:
            calculation = C1
            divisions = 0
            while calculation % 2 == 0:
                calculation = calculation / 2
                divisions = divisions + 1
                if divisions % 2 == 0:
                    num = C2
                else:
                    num = C1
        else:
            num = C1
            
    print("The computer chose", num)
    print("")
    if num == 0:
        print("Sorry, the computer won.")
    
    if num != 0:
        C1 = num - 1 
        C2 = int(num/2)
        if C1 == C2:
            playerChoice = int(input("Your only choice is " + str(C1) + ": "))
            num = playerChoice

            while playerChoice not in [C1]:
                print("That is not an option.") 
                playerChoice = int(input("Your only choice is " + str(C1) + ": "))

        else:
            playerChoice = int(input("Your choices are " + str(C1) + " or " + str(C2) + ": "))
            num = playerChoice

            while playerChoice not in [C1, C2]:
                print("That is not an option. Try again.")
                print("")
                playerChoice = int(input("Your choices are " + str(C1) + " or " + str(C2) + ": "))

            num = playerChoice
            
        print("You chose", num)
        print("")
        if num == 0:
            print("Congratulations! You win.")
               
print("Game over.")
print("Thank you for playing!")
