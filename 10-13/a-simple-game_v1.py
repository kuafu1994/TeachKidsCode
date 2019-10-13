
temp = input("guess a number between 1-100: ")
guess = int(temp)

while guess != 8:

    if guess > 8:
        print("The number you guessed was larger.")
    else:
        print("The number you guessed was less.")

    temp = input("You guess a wrong number, please eneter another number: ")
    guess = int(temp)    

print("Congraduate! You guessed the right number " + str(8))


