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
        
        changePlayer()
        
    if winner == "X" or winner == "O":
        print("Player " + winner + " won!")
    else:
        print("Its a tie!")
        
        
    
def handleTurns(currentPlayer):
    position = input("Player " + currentPlayer + "\n" +
                      "Choose a position from 1-9: " + "\n")

    position = int(position) - 1
    
    # Update the board
    board[position] = currentPlayer     
    
    displayBoard()
    
def checkGameOver():
    
    checkWin()
    checkTie()
    
    #set gameContinue to false
    
def checkWin():
    
    global winner
    
    #check rows
    #check columns
    #check diagonal
    
    return
    
def checkTie():
    return
    

def changePlayer(): 
    return


    




  
playGame()   
     
     
     
    
    
    