from tkinter import *
from tkinter import ttk
import random
import string

def generate_password():
    try:
        passlength = int(password_length.get())
        if passlength <= 0:
            result_label.config(text="Please enter a positive integer.")
            return
    except ValueError:
        result_label.config(text="Invalid input. Please enter a valid number.")
        return

    passcharacters = string.ascii_letters + string.digits + string.punctuation
    fullpassword = ''.join(random.choice(passcharacters) for _ in range(passlength))
    result_label.config(text="Your password is: " + fullpassword)

root = Tk()
root.title("Password Generator")

style = ttk.Style()
style.configure('TButton', padding=(10, 10), font=('Helvetica', 12))
style.configure('TLabel', font=('Helvetica', 12))

mainframe = ttk.Frame(root, padding="20 20 20 20")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

ttk.Label(mainframe, text="Enter the length for the password:", style='TLabel').grid(column=1, row=1, sticky=W, pady=10)
password_length = ttk.Entry(mainframe, width=7)
password_length.grid(column=2, row=1, sticky=(W, E))

ttk.Button(mainframe, text="Generate Password", style='TButton', command=generate_password).grid(column=2, row=2, sticky=W, pady=10)
result_label = ttk.Label(mainframe, text="", style='TLabel')
result_label.grid(column=1, row=3, columnspan=2, sticky=(W, E))

root.mainloop()
