# Game board created
# Display the board
# Keep track of scores
    # Check row
    # Check column
    # Check diagonal
    # Check if its a tie
# Alternate turns between players (option to play with another player or the computer)

# Creating a board
board = ["_","_","_",
         "_","_","_",
         "_","_","_"]

currentPlayer = "X"
gameContinues = True
winner = None



def displayBoard():
    print("Current Game Board \n")
    print(board[0] + " | " + board[1] + " | " + board[2] + "\n" +
          board[3] + " | " + board[4] + " | " + board[5] + "\n" +
          board[6] + " | " + board[7] + " | " + board[8] + "\n")
    
    
def playGame():
    
    # Display the initial board
    displayBoard()
    
    while gameContinues:
        
        handleTurns(currentPlayer)
        
        checkGameOver()
        if winner:
            break
        changePlayer()
        
    if winner == "X" or winner == "O":
        print("Player " + winner + " won!")
    else:
        print("Its a tie!")
        
        
    
def handleTurns(currentPlayer):
    while True:
        position = input("Player " + currentPlayer + "\n" +
                         "Choose a position from 1-9: " + "\n")
        if position.isdigit() and 1 <= int(position) <= 9:
            position = int(position) - 1

            if board[position] == "_":
                break
            else:
                print("Position already taken. Choose another position.")

    # Update the board
    board[position] = currentPlayer
    displayBoard()
    
def checkGameOver():
    
    checkWin()
    checkTie()
    
    #set gameContinue to false
    
def checkWin():
    
    checkRows()
    checkColumns()
    checkDiagonals()
    
    return

def checkRows():
    
    global winner
    for i in range(0, 7, 3):
        if board[i] == board[i + 1] == board[i + 2] != "_":
            winner = board[i]
            return
        
def checkColumns():
    global winner
    for i in range(3):
        if board[i] == board[i + 3] == board[i + 6] != "_":
            winner = board[i]
            return
        
def checkDiagonals():
    global winner
    if board[0] == board[4] == board[8] != "_":
        winner = board[0]
    elif board[2] == board[4] == board[6] != "_":
        winner = board[2]
    
    
    
def checkTie():
    global gameContinues
    if "_" not in board and not winner:
        gameContinues = False
    

def changePlayer(): 
    global currentPlayer
    if currentPlayer == "X":
        currentPlayer = "O"
    else:
        currentPlayer = "X"

  
playGame()   
     
     
     
    
    
    