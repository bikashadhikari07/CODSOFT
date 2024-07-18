from tkinter import *
from tkinter import ttk
import random
import string
import json

PASSWORD_FILE = "passwords.txt"

def generate_password():
    app_name_value = app_name.get()
    try:
        passlength = int(password_length.get())
        if passlength <= 0:
            gen_result_label.config(text="Please enter a positive integer.")
            return
    except ValueError:
        gen_result_label.config(text="Invalid input. Please enter a valid number.")
        return

    passcharacters = string.ascii_letters + string.digits + string.punctuation
    fullpassword = ''.join(random.choice(passcharacters) for _ in range(passlength))

    password_entry = {app_name_value: fullpassword}

    try:
        with open(PASSWORD_FILE, "r") as f:
            try:
                passwords = json.load(f)
                if not isinstance(passwords, dict):
                    passwords = {}
            except json.JSONDecodeError:
                passwords = {}
    except FileNotFoundError:
        passwords = {}

    passwords.update(password_entry)

    with open(PASSWORD_FILE, "w") as f:
        json.dump(passwords, f, indent=4)

    gen_result_label.config(text=f"Your password for {app_name_value} is: {fullpassword}. Saved!")
    display_saved_passwords()

def display_saved_passwords():
    try:
        with open(PASSWORD_FILE, "r") as f:
            passwords = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        passwords = {}

    for widget in pass_list_frame.winfo_children():
        widget.destroy()

    for app, password in passwords.items():
        ttk.Label(pass_list_frame, text=f"{app}: {password}", style='TLabel').pack(anchor=W)

root = Tk()
root.title("Password Manager")

style = ttk.Style()
style.configure('TButton', padding=(10, 10), font=('Helvetica', 12))
style.configure('TLabel', font=('Helvetica', 12))

notebook = ttk.Notebook(root)
notebook.pack(pady=10, expand=True)

# Password Generation Tab
gen_frame = ttk.Frame(notebook, padding="20 20 20 20")
gen_frame.pack(fill='both', expand=True)

ttk.Label(gen_frame, text="Enter the length for the password:", style='TLabel').grid(column=0, row=0, sticky=W, pady=10)
password_length = ttk.Entry(gen_frame, width=7)
password_length.grid(column=1, row=0, sticky=(W, E))

ttk.Label(gen_frame, text="Enter the app name:", style='TLabel').grid(column=0, row=1, sticky=W, pady=10)
app_name = ttk.Entry(gen_frame, width=20)
app_name.grid(column=1, row=1, sticky=(W, E))

ttk.Button(gen_frame, text="Generate Password", style='TButton', command=generate_password).grid(column=1, row=2, sticky=W, pady=10)
gen_result_label = ttk.Label(gen_frame, text="", style='TLabel')
gen_result_label.grid(column=0, row=3, columnspan=2, sticky=(W, E))

# Password List Tab
list_frame = ttk.Frame(notebook, padding="20 20 20 20")
list_frame.pack(fill='both', expand=True)

pass_list_frame = ttk.Frame(list_frame)
pass_list_frame.pack(fill='both', expand=True)

notebook.add(gen_frame, text='Generate Password')
notebook.add(list_frame, text='Saved Passwords')

display_saved_passwords()

root.mainloop()
