#Guess my number
#
#The computer picks a random number between 1 and 100
#The player tries to guess it and the computer lets 
#the player know if the guess is too high, too low 
#or right on the money

import random

#Explaining the game
print("\tWelcome to 'Guess My Number'!")
print("\nI'm thinking of a number between 1 and 1000")
print("Try to guess it in as few attempts as possible.\n")

#Setting the variables
the_number = random.randint(1, 10)
guess = int(input("Take a guess: "))
tries = 1

#Create a guessing loop
while guess != the_number:
    if guess > the_number:
        print("Lower...")
    else:
        print("Higher...")
    
    guess = int(input("Take a guess: "))
    tries += 1

print("You guessed it! The number was", the_number)
print("And it only took you", tries, "tries!\n")