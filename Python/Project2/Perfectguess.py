# Question
# Write a program that generates a random number and asks the user to guess it.

# If the player guesses higher than actual number, the program displays "Lower number please" Similarly, if the user's guess is too low, the program prints "higher number please" Similarly if the user's guess is too low, the program prints "Higher number please" when the user guess the correct number, the program displays the number of guesses the player used to arrive at the number


# Use the random module:


import random

n = random.randint(1, 100)
a = -1
guesses = 1

while(a != n):
    a = int(input("Guess a number"))
    if(a>n):
        print("Lower number please: ")
    elif(a>n):
        print("Give higher number please: ")
    guesses +=1

print(f"Guessed the number {n} Right though the attemt took were: {guesses}")