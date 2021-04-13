no_of_goes = 0

import random
myName = input("Hello! What is your name?")
number = random.randint(1, 100)

while no_of_goes <6:
    no_of_goes = no_of_goes + 1

    print( myName,  "I am thinking of a number between 1 and 100.")
    guess = int(input("Take a guess:") )

    if guess < number:
        print("You're too low. Better luck next time")

    elif guess > number:
        print("You're too high. Better luck next time")     

    elif guess == number:
        print("Good job,", myName, "You guessed my number")
    else:
       print("Sorry, I don't recognise that number")
    break
