rock = 1
paper = 2
scissors = 3

p1score = 0
p2score = 0

gameOver = 3

print("Rock = 1, Paper = 2, Scissors = 3")

while True:
    player1 = int(input("Player 1 - Enter your choice: "))
    player2 = int(input("Player 2 - Enter your choice: "))

    if player1 == player2:
        print("It's a tie!")
    elif (player1 == rock and player2 == scissors) or \
         (player1 == paper and player2 == rock) or \
         (player1 == scissors and player2 == paper):
        p1score += 1
        if p1score == gameOver:
            print("Player 1 is the Champion")

        print("Player 1 wins!" + str(p1score))
    else:

        p2score += 1
        if p2score == gameOver:
            print("Player 2 is the champion")
        print("Player 2 wins! " + str(p2score))

    command = input("Do you want to exit? (Yes/No): ")
    if command.lower() == "yes":
        break
