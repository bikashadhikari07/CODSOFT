from tkinter import *
from tkinter import ttk, messagebox
import random

# Initialize scores
user_score = 0
computer_score = 0
user_choice = ""

def set_user_choice(choice):
    global user_choice
    user_choice = choice
    game()  # Trigger the game function when a choice is made

def comp_choice():
    return random.choice(["Rock", "Paper", "Scissors"])

def game():
    global user_score, computer_score, user_choice
    computer_choice = comp_choice()
    result = determine_winner(user_choice, computer_choice)
    
    if result == "User wins!":
        user_score += 1
    elif result == "Computer wins!":
        computer_score += 1
    
    result_label.config(text=f"User choice: {user_choice}\nComputer choice: {computer_choice}\nResult: {result}")
    score_label.config(text=f"User Score: {user_score} | Computer Score: {computer_score}")
    play_again_prompt()

def determine_winner(user, computer):
    if user == computer:
        return "It's a tie!"
    elif (user == "Rock" and computer == "Scissors") or \
         (user == "Scissors" and computer == "Paper") or \
         (user == "Paper" and computer == "Rock"):
        return "User wins!"
    else:
        return "Computer wins!"

def play_again_prompt():
    play_again = messagebox.askyesno("Play Again", "Do you want to play another round?")
    if not play_again:
        root.quit()

root = Tk()
root.title("Rock Paper Scissors Game")

style = ttk.Style()
style.configure('TButton', padding=(10, 10), font=('Helvetica', 12))
style.configure('TLabel', font=('Helvetica', 12))

mainframe = ttk.Frame(root, padding="20 20 20 20")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

ttk.Label(mainframe, text="Choose your move:", style='TLabel').grid(column=1, row=0, columnspan=3, pady=10)

ttk.Button(mainframe, text="Rock", style='TButton', command=lambda: set_user_choice("Rock")).grid(column=1, row=1, sticky=W, padx=10, pady=10)
ttk.Button(mainframe, text="Paper", style='TButton', command=lambda: set_user_choice("Paper")).grid(column=2, row=1, sticky=W, padx=10, pady=10)
ttk.Button(mainframe, text="Scissors", style='TButton', command=lambda: set_user_choice("Scissors")).grid(column=3, row=1, sticky=W, padx=10, pady=10)

result_label = ttk.Label(mainframe, text="Make your choice to start the game!", style='TLabel')
result_label.grid(column=1, row=2, columnspan=3, pady=20)

score_label = ttk.Label(mainframe, text="User Score: 0 | Computer Score: 0", style='TLabel')
score_label.grid(column=1, row=3, columnspan=3, pady=10)

root.mainloop()
