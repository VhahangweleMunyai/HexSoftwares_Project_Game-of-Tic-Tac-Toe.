import tkinter as tk
from tkinter import messagebox
import random

# Function to check for a winner
def check_winner():
    for combo in [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]:
        if buttons[combo[0]]["text"] == buttons[combo[1]]["text"] == buttons[combo[2]]["text"] != "":
            for index in combo:
                buttons[index].config(bg="green")
            messagebox.showinfo("Tic-Tac-Toe", f"Player {buttons[combo[0]]['text']} wins!")
            return True
    return False

# Function for the computer's move based on difficulty
def computer_move():
    if difficulty == "Easy":
        easy_move()
    elif difficulty == "Medium":
        medium_move()
    elif difficulty == "Hard":
        hard_move()

# Easy move: Random move
def easy_move():
    empty_buttons = [i for i in range(9) if buttons[i]["text"] == ""]
    if empty_buttons:
        index = random.choice(empty_buttons)
        buttons[index]["text"] = current_player
        if check_winner():
            return
        toggle_player()

# Medium move: Random move or block player
def medium_move():
    # Check for possible winning moves for the player and block them
    for combo in [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]:
        if (buttons[combo[0]]["text"] == buttons[combo[1]]["text"] != "" and buttons[combo[2]]["text"] == ""):
            buttons[combo[2]]["text"] = current_player
            if check_winner():
                return
            toggle_player()
            return
        if (buttons[combo[0]]["text"] == buttons[combo[2]]["text"] != "" and buttons[combo[1]]["text"] == ""):
            buttons[combo[1]]["text"] = current_player
            if check_winner():
                return
            toggle_player()
            return
        if (buttons[combo[1]]["text"] == buttons[combo[2]]["text"] != "" and buttons[combo[0]]["text"] == ""):
            buttons[combo[0]]["text"] = current_player
            if check_winner():
                return
            toggle_player()
            return

    # If no blocking move, make a random move
    easy_move()

# Hard move: Use strategy to win or block
def hard_move():
    # Check if the computer can win
    for combo in [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]:
        if (buttons[combo[0]]["text"] == buttons[combo[1]]["text"] == current_player and buttons[combo[2]]["text"] == ""):
            buttons[combo[2]]["text"] = current_player
            if check_winner():
                return
            toggle_player()
            return
        if (buttons[combo[0]]["text"] == buttons[combo[2]]["text"] == current_player and buttons[combo[1]]["text"] == ""):
            buttons[combo[1]]["text"] = current_player
            if check_winner():
                return
            toggle_player()
            return
        if (buttons[combo[1]]["text"] == buttons[combo[2]]["text"] == current_player and buttons[combo[0]]["text"] == ""):
            buttons[combo[0]]["text"] = current_player
            if check_winner():
                return
            toggle_player()
            return

    # If player can win, block it
    for combo in [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]:
        if (buttons[combo[0]]["text"] == buttons[combo[1]]["text"] != "" and buttons[combo[2]]["text"] == ""):
            buttons[combo[2]]["text"] = current_player
            if check_winner():
                return
            toggle_player()
            return
        if (buttons[combo[0]]["text"] == buttons[combo[2]]["text"] != "" and buttons[combo[1]]["text"] == ""):
            buttons[combo[1]]["text"] = current_player
            if check_winner():
                return
            toggle_player()
            return
        if (buttons[combo[1]]["text"] == buttons[combo[2]]["text"] != "" and buttons[combo[0]]["text"] == ""):
            buttons[combo[0]]["text"] = current_player
            if check_winner():
                return
            toggle_player()
            return

    # If no immediate win or block, make a random move
    easy_move()

# Function to handle button clicks by the player
def button_click(index):
    global winner
    if buttons[index]["text"] == "" and not winner:
        buttons[index]["text"] = current_player
        if check_winner():
            winner = True
        else:
            toggle_player()
            computer_move()

# Function to toggle between players
def toggle_player():
    global current_player
    current_player = "O" if current_player == "X" else "X"
    label.config(text=f"Player {current_player}'s turn")

# Main application setup
root = tk.Tk()
root.title("Tic-Tac-Toe")

# Difficulty selection
difficulty = "Hard" # Change this to "Easy", "Medium", or "Hard" to set difficulty level

buttons = [tk.Button(root, text="", font=("normal", 25), width=6, height=2,
                     command=lambda i=i: button_click(i)) for i in range(9)]

for i, button in enumerate(buttons):
    button.grid(row=i // 3, column=i % 3)

current_player = "X"  # Player is "X" (user)
winner = False  # Initially, there is no winner

label = tk.Label(root, text=f"Player {current_player}'s turn", font=("normal", 16))
label.grid(row=3, column=0, columnspan=3)

root.mainloop()
