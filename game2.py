# Guessing a random number
import random
number = random.randint(1,10)
count =1
guess = int(input("Guess a number: "))
while(True):
    if(guess>number):
        print("Guess a another number!. This is to big")
        count+=1
    elif(guess<number):
        print("Guess a another number! This is to less")
        count+=1
    else:
        print("You win! You guessed right number")
    break