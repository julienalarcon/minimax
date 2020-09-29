from tictactoe import *

# main
print("#########################")
print("Starting TicTacToe Game !")
print("#########################")

board = newGame()

# Player choice
myPlayer, computer = choosePlayer()

# Start (X always start)
while True:
    result = gameTurn(myPlayer, computer, board)
    if not result is None:
        break



print("")
print("#########################")
print("Game is finished")
printBoard(board)
if result == 0:
    print("It's a tie !")
elif (result == 1 and myPlayer == "X") or (result == -1 and myPlayer == "O"):
    print("You win !!")
else:
    print("You loose....")

print("#########################")
