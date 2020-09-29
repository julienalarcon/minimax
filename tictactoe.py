import copy

# Constants
EMPTY_CELL = "_"

# Variables
boardLineSize = 3
currentPlayer = "X"

# X winner == 1 - So X will try to maximize
# O winner == -1, so O will try to minimize

# init game
def newGame():
    return [EMPTY_CELL] * boardLineSize * boardLineSize


# Choose which player I am
def choosePlayer():
    while True:
        print("Choose your player (X / O):")
        myPlayer = input()
        if(not myPlayer in ["X", "O"]):
            print("Wrong input, enter O or X")
        else:
            break

    if myPlayer == "X":
        computer = "O"
    else:
        computer = "X"

    return myPlayer, computer


def gameTurn(myPlayer, computer, board):

    global currentPlayer

    # Check if game is finished
    moves = [i for i, val in enumerate(board) if val == EMPTY_CELL]
    winnerScore = getWinnerScore(board)

    if winnerScore:
        return winnerScore

    if not moves:
        return 0

    # Else we play
    print("")
    print("# Current board : ")
    printBoard(board)

    if myPlayer == currentPlayer: # my turn
        while True:
            print("Enter coordinates for your next point (x,y)")
            try:
                myCoordinates = input()
                myX, myY = int(myCoordinates.split(",")[0]),int(myCoordinates.split(",")[1])
                myPoint = myY*boardLineSize + myX

                if board[myPoint] != EMPTY_CELL:
                    print("Point " + myCoordinates + " is already taken !!")
                    continue

                break
            except ValueError:
                print("Enter valid coordinates x,y !!")
                continue

        board[myPoint] = myPlayer

    else: # Computer's turn
        print("")
        print("Computer plays...")
        bestMove = -1

        if computer == "X":
            bestScore = -100
        else:
            bestScore = 100

        for move in moves:
            boardCopy = copy.copy(board)
            boardCopy[move] = computer
            score = minimax(boardCopy, myPlayer)
            #print(f"Score for {move} is {score}")
            if computer == "X":
                if score > bestScore:
                    bestMove = move
                    bestScore = score
            else:
                if score < bestScore:
                    bestMove = move
                    bestScore = score

        board[bestMove] = computer

    if currentPlayer == "X":
        currentPlayer = "O"
    else:
        currentPlayer = "X"

    return None


# Computer intelligence
def minimax(board, player):
    # Get possible moves
    moves = [i for i, val in enumerate(board) if val == EMPTY_CELL]
    winnerScore = getWinnerScore(board)

    if winnerScore: # if winner, we return the score
        return winnerScore

    if not moves: # If game over (no moves) its a tie
        return 0

    if player == "X": # Try to maximize
        score = -100
        for move in moves:
            boardCopy = copy.copy(board)
            boardCopy[move] = "X"
            score = max(score, minimax(boardCopy, "O"))
    else: # try to minimize
        score = 100
        for move in moves:
            boardCopy = copy.copy(board)
            boardCopy[move] = "O"
            score = min(score, minimax(boardCopy, "X"))

    return score


# print the board in a friendly way
def printBoard(board):
    for i in range(0, boardLineSize):

        if i > 0:
            print(" "+str(i)+" ", end="")
        elif i == 0:
            print("   ", end="")
            for j in range(0, boardLineSize):
                print(" "+str(j), end=" ")
            print("")
            print (" "+str(i), end=" ")

        for j in range(0, boardLineSize):
            print(" ", end="")
            print(board[(i*boardLineSize)+j], end=" ")

        print("")

# Check if any winning position
def getWinnerScore(board):
    winningPositions = ""

    # Lines
    for i in range(0, boardLineSize):
        winningPositions += "".join(board[(boardLineSize*i):boardLineSize*(i+1)]) + " "

    # Columns
    for i in range(0, boardLineSize):
        for j in range(0, boardLineSize):
            winningPositions += board[(j*boardLineSize)+i]
        winningPositions += " "

    # Diagonals
    diag1 = "" # Top left to bottom right
    diag2 = "" # Top right to bottom left
    for i in range(0, boardLineSize):
        diag1 += board[i*(boardLineSize+1)]
        diag2 += board[(i+1)*(boardLineSize-1)]

    winningPositions += diag1 + " " + diag2

    # Do we have a winner ?
    if ("X"*boardLineSize) in winningPositions:
        return 1
    elif ("O"*boardLineSize) in winningPositions:
        return -1
    else:
        return 0

def setBoardLineSize(newSize):
    global boardLineSize
    boardLineSize = newSize
