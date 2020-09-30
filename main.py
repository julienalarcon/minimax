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
print("Game finished, results ")
print("#########################")

printBoard(board)

winner = getWinner(board)

print("")

if winner == "TIE":
    print("It's a tie !")
elif winner == myPlayer:
    print("You win !!")
else:
    print("You loose....")

print("")

print("#########################")
print("End ")
print("#########################")
