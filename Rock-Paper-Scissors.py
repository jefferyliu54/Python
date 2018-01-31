#Objects: Honeybee, Mosquito, Person, Bear, Spider
#Explanations:
    #Honeybee stings Person
    #Honeybee outlives Mosquito because humans kill mosquitoes when they bite them

    #Mosquito bites Bear
    #Mosquito bites Person

    #Person hunts and kills Bear
    #Person runs through spiderwebs and kills Spider

    #Bear raid beehives and eat the honey of the Honeybee
    #Bear breaks spiderwebs and kills Spider 

    #Spider catches and eats Mosquito
    #Spider catches and eats Honeybee

from random import *

print("Welcome to the 5 Way game of Rock-Paper-Scissors!")
times = int(input("How many times do you want to play the game?: "))
playerScore = 0
computerScore = 0 
    
for x in range(times):
    print("")
    playerMove = input("Choose the object that you wish to play (H/M/P/B/S): ")
    print("You chose", playerMove)

    while playerMove not in ["H", "M", "P", "B", "S"]:
        print("Sorry, that's not an option.")
        print("")
        playerMove = input("Choose the object that you wish to play (H/M/P/B/S): ")

    computerMove = choice(["H", "M", "P", "B", "S"])
    print("The computer chose", computerMove)

    if playerMove == computerMove:
        print("It's a tie!")

    elif playerMove == "H":
        if computerMove in ["B", "S"]:
            print("Computer won this round.")
            computerScore = computerScore + 1  
        else:
            print("You won this round!")
            playerScore = playerScore + 1

    elif playerMove == "M":
        if computerMove in ["H", "S"]:
            print("Computer won this round.")
            computerScore = computerScore + 1  
        else:
            print("You won this round!")
            playerScore = playerScore + 1

    elif playerMove == "P":
        if computerMove in ["H", "M"]:
            print("Computer won this round.")
            computerScore = computerScore + 1
        else:
            print("You won this round!")
            playerScore = playerScore + 1

    elif playerMove == "B":
        if computerMove in ["M", "P"]:
            print("Computer won this round.")
            computerScore = computerScore + 1
        else:
            print("You won this round!")
            playerScore = playerScore + 1

    else:
        if computerMove in ["P", "B"]:
            print("Computer won this round.")
            computerScore = computerScore + 1
        else:
            print("You won this round!")
            playerScore = playerScore + 1

print("")
print("Your final score is:", playerScore)
print("The computer's final score is:", computerScore)

if playerScore > computerScore:
    print("Congratulations! You won the whole match.")

else:
    print("Sorry, the computer won the whole match.")


    

    

