import tkinter as tk
from tkinter import messagebox

#constants for the players
HUMAN = 'O'
AI = 'X'
EMPTY = ' '

#creation of main window
root = tk.Tk()
root.title("Tic-Tac-Toe")

#creation of 3x3 grid of buttons
buttons = [[None for _ in range(3)] for _ in range(3)]
board = [[EMPTY for _ in range(3)] for _ in range(3)]

def check_winner(b):
    """Check if there is a winner or a draw"""
    #check rows, colums, and diagonals
    for row in range(3):
        if b[row][0] == b[row][1] == b[row][2] != EMPTY:
            return b[row][0]
        
    for col in range(3):
        if b[0][col] == b[1][col] == b[2][col] != EMPTY:
            return b[0][col]
    if b[0][0] == b[1][1] == b[2][2] != EMPTY:
        return b[0][0]
    if b[0][2] == b[1][1] == b[2][0] != EMPTY:
        return b[0][2]
    if all(b[row][col] != EMPTY for row in range(3) for col in range(3)):
        return 'Draw'
    return None

def minimax(b, is_maximizing):
    #minimax algorithm to evaluate moves.
    winner = check_winner(b)
    if winner == AI:
        return 1
    elif winner == HUMAN:
        return -1
    elif winner =='Draw':
        return 0
    
    if is_maximizing:
        best_score = float('-inf')
        for row in range(3):
            for col in range(3):
                if b[row][col] == EMPTY:
                    b[row][col] = AI
                    score = minimax(b,False)
                    b[row][col] = EMPTY
                    best_score = max(best_score, score)
        return best_score
    else:
        best_score = float('inf')
        for row in range(3):
            for col in range(3):
                if b[row][col] == EMPTY:
                    b[row][col] = HUMAN
                    score = minimax(b, True)
                    b[row][col] = EMPTY
                    best_score = min(best_score, score)
        return best_score

def ai_move():
    #Make the best move for the AI
    best_score = float('-inf')
    best_move = None
    for row in range(3):
        for col in range(3):
            if board[row][col] == EMPTY:
                board[row][col] = AI
                score = minimax(board, False)
                board[row][col] = EMPTY
                if score > best_score:
                    best_score = score
                    best_move = (row, col)
    if best_move:
        row, col = best_move
        board[row][col] = AI
        buttons[row][col].config(text=AI, state='disabled')
        winner = check_winner(board)
        if winner:
            end_game(winner)

def human_move(row, col):
    #Handle human move.
    if board[row][col] == EMPTY:
        board[row][col] = HUMAN
        buttons[row][col].config(text=HUMAN, state='disabled')
        winner = check_winner(board)
        if winner:
            end_game(winner)
        else:
            ai_move()

def end_game(winner):
    #Display the game result and reset the board.    
    if winner == 'Draw':
        messagebox.showinfo("Tic-Tac-Toe", "It's a draw!")
    else:
        messagebox.showinfo("Tic-Tac-Toe", f"The winner is {winner}!")
    reset_board()

def reset_board():
    #Reset the board for a new game.
    global board
    board = [[EMPTY for _ in range(3)] for _ in range(3)]
    for row in range(3):
        for col in range(3):
            buttons[row][col].config(text=EMPTY, state='normal')

#creation of buttons and place them in the grid
for row in range(3):
    for col in range(3):
        button = tk.Button(root, text=EMPTY, font='normal 20', width=5, height=2,
                           command=lambda r=row, c=col: human_move(r, c))
        button.grid(row=row, column=col)
        buttons[row][col] = button

#main loop
reset_board()
root.mainloop()