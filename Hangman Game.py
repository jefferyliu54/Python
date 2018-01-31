import random

playAgain = "Y"
while playAgain in ["Y", "y", "yes"]:
    
    print("Hello! Welcome to the Python Game of Hangman!")
    rules = input("Would you like to see the rules? (Y/N): ")
    print("")
    
    if rules in ["Y", "y"]:
        print("In this game, you must guess an unknown word.")
        print("The number of blanks will indicate the number of letters in the word.")
        print("You have to guess one letter at a time.")
        print("If you guess a correct letter, the letter will show up in the word.")
        print("If you guess an incorrect letter, you will lose one turn.")
        print("You have to try and guess the word before you run out of turns.")
        print("Good luck!")
        print("")

    words = ("python", "mathematics", "fabricate", "destruction", "prejudice", "application", "electronics", "continental", "extraterrestrial", "shareholder", "appointment", "countryside")
                
    secretWord = random.choice(words)
    lettersInWord = "-" * len(secretWord)
    lettersGuessed = []
    guesses = 10
    wins = 0

    print("The word you are trying to guess is: ", lettersInWord)
    print("")
    
    while guesses > 0:
        
        letters = input("Guess a letter: ")
        print("")

        while letters in lettersGuessed:
            print("You guessed the letter", letters, "already.")
            letters = input("Guess a different letter: ")
            print("")

        while letters not in ["A","a","B","b","C","c","D","d","E","e","F","f","G","g","H","h","I","i","J","j","K","k","L","l","M","m","N","n","O","o","P","p","Q","q","R","r","S","s","T","t","U","u","V","v","W","w","X","x","Y","y","Z","z"]:
            print(letters, "is not a letter.")
            letters = input("Guess a letter: ")
                    
        lettersGuessed.append(letters) 
                  
        if letters in secretWord:
            print("The letter", letters, "is in the word!")
            correctLetter = ""
            for i in range(len(secretWord)):
                if letters == secretWord[i]:
                    correctLetter = correctLetter + letters
                else:
                    correctLetter = correctLetter + lettersInWord[i]
            lettersInWord = correctLetter
            print("The updated word is: ", lettersInWord)
            print("")
            
        else:
            guesses = guesses - 1
            print("The letter", letters, "is not in the word.")
            print("You now have", guesses, "more guesses.")
            print("Try again.")
            print("")

        print("You have guessed these letters so far: ", lettersGuessed)

    if lettersInWord == secretWord:
        print("You guessed the word!")
        wins = wins + 1
        
    else:
        print("You ran out of guesses.")
        print("Game over!")
        print("The word was", secretWord)
        
    playAgain = input("Would you like to play again? (Y/N): ")

print("Thanks for playing!")
print("You successfully guessed the word", wins, "times.")
