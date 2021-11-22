import random

def game(computer,playerChoice):
    if computer==playerChoice:
        return None

    elif computer=="r":
        if playerChoice=="s":
            return False
        elif playerChoice=="p":
            return True

    elif computer=="p":
        if playerChoice=="r":
            return False
        elif playerChoice=="s":
            return True
    
    elif computer=="s":
        if playerChoice=="p":
            return False
        elif playerChoice=="r":
            return True

randomNumber=random.randint(1,3)
if randomNumber==1:
    computer="r"
elif randomNumber==2:
    computer="p"
elif randomNumber==3:
    computer="s"

print("computer's turn: Rock(r), Paper(p) or Scissor(s)?")
playerChoice=input("Your turn: Rock(r), Paper(p) or Scissor(s)?\nYou chose: ")
print("computer chose:",str(computer))

gameWin=game(computer,playerChoice)

if gameWin==None:
    print("The game is a tie")
elif gameWin:
    print("You win")
else:
    print("You lose")

