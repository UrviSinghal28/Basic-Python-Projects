import random

playerWins=0
computerWins=0

def game(computer, playerChoice):
    if computer == playerChoice:
        return None

    elif computer == "r":
        if playerChoice == "s":
            return False
        elif playerChoice == "p":
            return True

    elif computer == "p":
        if playerChoice == "r":
            return False
        elif playerChoice == "s":
            return True

    elif computer == "s":
        if playerChoice == "p":
            return False
        elif playerChoice == "r":
            return True


randomNumber = random.randint(1, 3)
if randomNumber == 1:
    computer = "r"
elif randomNumber == 2:
    computer = "p"
elif randomNumber == 3:
    computer = "s"

print('Lets play a game of rock, paper and scissors!\n')

while True:
    start=input("Type 'y' to continue and 'q' to quit:\n").lower()
    if start=='q':
        break
    elif start not in (['y','q']):
        continue
    else:
        print("Computer's turn: Rock(r), Paper(p) or Scissor(s)?")
        playerChoice = input("Your turn: Rock(r), Paper(p) or Scissor(s)?\nYou chose: ")
        print("Computer chose:", str(computer))

        gameWin = game(computer, playerChoice)

        if gameWin == None:
            print("The game is a tie\n")
        elif gameWin:
            print("You win\n")
            playerWins+=1
        else:
            print("You lose\n")
            computerWins+=1
    

print("you won", playerWins, "times")
print("Computer won", computerWins, "times")
print('Thank you for playing!')

