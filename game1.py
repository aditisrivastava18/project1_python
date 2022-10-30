import random
import math


print('Hello! What is your name?')
myName = input()

# taking small and large inputs.
B = int(input("Enter Lower Bound"))

A = int(input("Enter Upper Bound"))

# generating random values
x = random.randint(B , A)

# prediction depends upon range.

print("\n\tYou've only ", round(math.log(A - B + 1, 2))," chances to guess the number!\n")

#initializing no. of guesses
count = 0

while count < math.log(A - B + 1, 2):
    count += 1

 
    predict_the_number = int(input("Guess a number:- "))
 
    if x == predict_the_number:
        print("Congratulations!!" +  myName + "\t"  +  "you did it in",count, " try")
        # Once guessed , loop willbreak here.
        break
    elif x > predict_the_number:
        print("You guessed too small!")
    elif x < predict_the_number:
        print("You Guessed too high!")

#if number prediction is more than required guesses,print this output!!

if count >= math.log(A - B + 1, 2):
    print("\nThe number is %d" % x)
    print("\tBetter Luck Next time!")