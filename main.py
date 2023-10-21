# Tic Tac Toe Game in Python

# Defining the global variables
board = ["_","_","_",
         "_","_","_",
         "_","_","_"]

currentPlayer = "X"
gameContinues = True
winner = None


# Function to display the board
def displayBoard():
    print("Current Game Board \n")
    print(board[0] + " | " + board[1] + " | " + board[2] + "\n" +
          board[3] + " | " + board[4] + " | " + board[5] + "\n" +
          board[6] + " | " + board[7] + " | " + board[8] + "\n")
    
 # Function for playing the game    
def playGame():
    
    # Display the initial board
    displayBoard()
    # Looping until the game stops
    while gameContinues:
        
        # Changing between the player turns
        handleTurns(currentPlayer)
        #Check if the game is over or not after every turn
        checkGameOver()
        if winner:
            break
        changePlayer()
    # If game over print the results    
    if winner == "X" or winner == "O":
        print("Player " + winner + " won!")
    else:
        print("Its a tie!")
        
        
# Function to change between the turns of the player    
def handleTurns(currentPlayer):
    while True:
        # Getting the player input
        position = input("Player " + currentPlayer + "\n" +
                         "Choose a position from 1-9: " + "\n")
        # Checking if the input is valid and within the range of the board
        if position.isdigit() and 1 <= int(position) <= 9:
            position = int(position) - 1

            if board[position] == "_":
                break
            else:
                print("Position already taken. Choose another position.")

    # Update the board
    board[position] = currentPlayer
    # Display the board
    displayBoard()
 
# Functionto check if the game is over    
def checkGameOver():
    
    # Call function to check if there is a win
    checkWin()
    # Otherwise call the function to check for a tie
    checkTie()
    
# Function to check the win
def checkWin():
    global winner
    # Check rows
    for i in range(0, 7, 3):
        if board[i] == board[i + 1] == board[i + 2] != "_":
            winner = board[i]
            return

    # Check columns
    for i in range(3):
        if board[i] == board[i + 3] == board[i + 6] != "_":
            winner = board[i]
            return

    # Check diagonals
    if board[0] == board[4] == board[8] != "_":
        winner = board[0]
    elif board[2] == board[4] == board[6] != "_":
        winner = board[2]

# Function to check for a tie        
def checkTie():
    global gameContinues
    if "_" not in board and not winner:
        gameContinues = False
    
# Function to change the player symbol after every turn
def changePlayer(): 
    global currentPlayer
    if currentPlayer == "X":
        currentPlayer = "O"
    else:
        currentPlayer = "X"

# Execute the game 
playGame()   
     
     
     
    
    
    