import random


randNum = random.randint(1,9)
guessCount = 0


while True:
    print("The random number is " + str(randNum))
    guess = int(input("Guess the number from 1 -9 "))
    guessCount += 1
    if randNum == guess:
        print("Nice one you got it right " + str(guessCount) + " is your number of  guesses")
        command = input("Do you want to exit?? Y or N")
        command.lower()
        if command == "y":
            break

    elif guess > randNum:
        print("So Cold")
    else:
        print("So Hot")







