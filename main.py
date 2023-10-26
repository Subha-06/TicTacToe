import tkinter as tk

# Creating the main window
root = tk.Tk()
root.title("Tic Tac Toe")
root.geometry("500x500")  # Adjusting the initial size of the window

# Defining the global variables
board = [" "]*9

currentPlayer = "X"
gameContinues = True
winner = None

# Function to handle the button click
def on_button_click(i):
    global currentPlayer, winner, gameContinues
    if gameContinues and board[i] == " ":
        board[i] = currentPlayer
        buttons[i].config(text=currentPlayer)
        checkGameOver()
        if winner:
            gameContinues = False
            print(f"Player {winner} won!")
        changePlayer()

# Function to check if the game is over
def checkGameOver():
    checkWin()
    checkTie()

# Function to check the win
def checkWin():
    global winner
    for i in range(0, 7, 3):
        if board[i] == board[i + 1] == board[i + 2] != " ":
            winner = board[i]
            return
    for i in range(3):
        if board[i] == board[i + 3] == board[i + 6] != " ":
            winner = board[i]
            return
    if board[0] == board[4] == board[8] != " ":
        winner = board[0]
    elif board[2] == board[4] == board[6] != " ":
        winner = board[2]

# Function to check for a tie
def checkTie():
    global gameContinues
    if " " not in board and not winner:
        gameContinues = False
        print("It's a tie!")

# Function to change the player symbol after every turn
def changePlayer(): 
    global currentPlayer
    if currentPlayer == "X":
        currentPlayer = "O"
    else:
        currentPlayer = "X"

# Function to start a new game
def new_game():
    global board, currentPlayer, gameContinues, winner
    for i in range(9):
        buttons[i].config(text=" ")
    board = [" "]*9
    currentPlayer = "X"
    gameContinues = True
    winner = None

# Function to quit the game
def quit_game():
    root.quit()

# Creating the buttons for the board
buttons = []
for i in range(9):
    row = i // 3
    col = i % 3
    button = tk.Button(root, text=board[i], font=("Helvetica", 70), width=2, height=1, command=lambda i=i: on_button_click(i))
    button.grid(row=row, column=col, sticky="nsew")  # Modifying the sticky parameter
    buttons.append(button)

# Configuring rows and columns to expand proportionally
for i in range(3):
    root.grid_rowconfigure(i, weight=1)
    root.grid_columnconfigure(i, weight=1)

# Creating a menu
menu = tk.Menu(root)
root.config(menu=menu)
file_menu = tk.Menu(menu, tearoff=0)
menu.add_cascade(label="Menu", menu=file_menu)
file_menu.add_command(label="New Game", command=new_game)
file_menu.add_separator()
file_menu.add_command(label="Quit", command=quit_game)

# Running the main loop
root.mainloop()
