import random

value = random.randint(1, 100)
temp = input("guess a number between 1-100: ")
guess = int(temp)

while guess != value:

    if guess > value:
        print("The number you guessed was larger.")
    else:
        print("The number you guessed was less.")

    temp = input("You guess a wrong number, please eneter another number: ")
    guess = int(temp)    

print("Congraduate! You guessed the right number " + str(value))


