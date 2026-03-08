import tkinter as tk
from tkinter import messagebox

# Create window
root = tk.Tk()
root.title("Tic Tac Toe")

# Game variables
player = "X"
buttons = [[None for _ in range(3)] for _ in range(3)]

# Check winner
def check_winner():
    for i in range(3):
        if buttons[i][0]["text"] == buttons[i][1]["text"] == buttons[i][2]["text"] != "":
            return True
        if buttons[0][i]["text"] == buttons[1][i]["text"] == buttons[2][i]["text"] != "":
            return True

    if buttons[0][0]["text"] == buttons[1][1]["text"] == buttons[2][2]["text"] != "":
        return True
    if buttons[0][2]["text"] == buttons[1][1]["text"] == buttons[2][0]["text"] != "":
        return True

    return False

# Check draw
def check_draw():
    for row in buttons:
        for btn in row:
            if btn["text"] == "":
                return False
    return True

# Button click
def click(row, col):
    global player

    if buttons[row][col]["text"] == "":
        buttons[row][col]["text"] = player

        if check_winner():
            messagebox.showinfo("Winner", f"Player {player} wins!")
            reset_game()
            return

        if check_draw():
            messagebox.showinfo("Draw", "It's a Draw!")
            reset_game()
            return

        player = "O" if player == "X" else "X"

# Reset game
def reset_game():
    global player
    player = "X"
    for row in buttons:
        for btn in row:
            btn["text"] = ""

# Create grid buttons
for i in range(3):
    for j in range(3):
        btn = tk.Button(root, text="", font=("Arial", 30), width=5, height=2,
                        command=lambda r=i, c=j: click(r, c))
        btn.grid(row=i, column=j)
        buttons[i][j] = btn

root.mainloop()