import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import json

# File path for storing contacts
CONTACTS_FILE = "contacts.txt"

def save_contacts():
    with open(CONTACTS_FILE, "w") as f:
        json.dump(contacts, f)

def load_contacts():
    try:
        with open(CONTACTS_FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def add_contact():
    name = entry_name.get().strip()
    phone = entry_phone.get().strip()
    email = entry_email.get().strip()
    address = entry_address.get().strip()

    if name and phone:
        contact = {"Name": name, "Phone": phone, "Email": email, "Address": address}
        contacts.append(contact)
        save_contacts()  # Save updated contacts to file
        update_contact_list()
        entry_name.delete(0, tk.END)
        entry_phone.delete(0, tk.END)
        entry_email.delete(0, tk.END)
        entry_address.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter at least Name and Phone.")

def update_contact_list():
    # Clear existing treeview items
    for item in tree.get_children():
        tree.delete(item)

    # Insert updated contacts into treeview
    for idx, contact in enumerate(contacts, start=1):
        tree.insert("", "end", iid=idx, values=(idx, contact["Name"], contact["Phone"], contact["Email"], contact["Address"]))

def delete_contact():
    selected_item = tree.selection()
    if selected_item:
        contact_index = int(tree.item(selected_item, "values")[0]) - 1
        del contacts[contact_index]
        save_contacts()  # Save updated contacts to file
        update_contact_list()

def edit_contact():
    selected_item = tree.selection()
    if selected_item:
        contact_index = int(tree.item(selected_item, "values")[0]) - 1
        contact = contacts[contact_index]

        edit_window = tk.Toplevel(root)
        edit_window.title("Edit Contact")

        ttk.Label(edit_window, text="Name:").grid(row=0, column=0, padx=10, pady=10, sticky="e")
        entry_name_edit = ttk.Entry(edit_window, width=30)
        entry_name_edit.grid(row=0, column=1, padx=10, pady=10)
        entry_name_edit.insert(0, contact["Name"])

        ttk.Label(edit_window, text="Phone:").grid(row=1, column=0, padx=10, pady=10, sticky="e")
        entry_phone_edit = ttk.Entry(edit_window, width=30)
        entry_phone_edit.grid(row=1, column=1, padx=10, pady=10)
        entry_phone_edit.insert(0, contact["Phone"])

        ttk.Label(edit_window, text="Email:").grid(row=2, column=0, padx=10, pady=10, sticky="e")
        entry_email_edit = ttk.Entry(edit_window, width=30)
        entry_email_edit.grid(row=2, column=1, padx=10, pady=10)
        entry_email_edit.insert(0, contact["Email"])

        ttk.Label(edit_window, text="Address:").grid(row=3, column=0, padx=10, pady=10, sticky="e")
        entry_address_edit = ttk.Entry(edit_window, width=30)
        entry_address_edit.grid(row=3, column=1, padx=10, pady=10)
        entry_address_edit.insert(0, contact["Address"])

        def save_update():
            updated_contact = {
                "Name": entry_name_edit.get().strip(),
                "Phone": entry_phone_edit.get().strip(),
                "Email": entry_email_edit.get().strip(),
                "Address": entry_address_edit.get().strip()
            }
            contacts[contact_index] = updated_contact
            save_contacts()  # Save updated contacts to file
            update_contact_list()
            edit_window.destroy()

        ttk.Button(edit_window, text="Save", command=save_update).grid(row=4, column=0, columnspan=2, pady=10)

def search_contact():
    for item in tree_search.get_children():
        tree_search.delete(item)

    search_query = entry_search.get().strip().lower()
    matched_contacts = [contact for contact in contacts if search_query in contact["Name"].lower() or search_query in contact["Phone"]]

    for idx, contact in enumerate(matched_contacts, start=1):
        tree_search.insert("", "end", values=(idx, contact["Name"], contact["Phone"], contact["Email"], contact["Address"]))

# Initialize tkinter root window
root = tk.Tk()
root.title("Contact Book")
root.geometry("1000x400")

# Load contacts from file
contacts = load_contacts()

# Create notebook for tabs
notebook = ttk.Notebook(root)
notebook.pack(expand=True, fill='both')

# Add Contact Tab
tab_add_contact = ttk.Frame(notebook)
notebook.add(tab_add_contact, text='Add Contact')

# View Contacts Tab
tab_view_contacts = ttk.Frame(notebook)
notebook.add(tab_view_contacts, text='View Contacts')

# Search Contacts Tab
tab_search_contacts = ttk.Frame(notebook)
notebook.add(tab_search_contacts, text='Search Contacts')

# Labels and Entries for Add Contact Tab
ttk.Label(tab_add_contact, text="Name:").grid(row=0, column=0, padx=10, pady=10, sticky="e")
entry_name = ttk.Entry(tab_add_contact, width=30)
entry_name.grid(row=0, column=1, padx=10, pady=10)

ttk.Label(tab_add_contact, text="Phone:").grid(row=1, column=0, padx=10, pady=10, sticky="e")
entry_phone = ttk.Entry(tab_add_contact, width=30)
entry_phone.grid(row=1, column=1, padx=10, pady=10)

ttk.Label(tab_add_contact, text="Email:").grid(row=2, column=0, padx=10, pady=10, sticky="e")
entry_email = ttk.Entry(tab_add_contact, width=30)
entry_email.grid(row=2, column=1, padx=10, pady=10)

ttk.Label(tab_add_contact, text="Address:").grid(row=3, column=0, padx=10, pady=10, sticky="e")
entry_address = ttk.Entry(tab_add_contact, width=30)
entry_address.grid(row=3, column=1, padx=10, pady=10)

btn_add_contact = ttk.Button(tab_add_contact, text="Add Contact", command=add_contact)
btn_add_contact.grid(row=4, column=0, columnspan=2, pady=10)

# Treeview for View Contacts Tab
tree = ttk.Treeview(tab_view_contacts, columns=("SN", "Name", "Phone", "Email", "Address"), show="headings")
tree.heading("SN", text="SN")
tree.heading("Name", text="Name")
tree.heading("Phone", text="Phone")
tree.heading("Email", text="Email")
tree.heading("Address", text="Address")
tree.pack(expand=True, fill='both')

btn_delete_contact = ttk.Button(tab_view_contacts, text="Delete Contact", command=delete_contact)
btn_delete_contact.pack(pady=10)

btn_edit_contact = ttk.Button(tab_view_contacts, text="Edit Contact", command=edit_contact)
btn_edit_contact.pack(pady=10)

update_contact_list()  # Update treeview with loaded contacts

# Search Contacts Tab
ttk.Label(tab_search_contacts, text="Search Contact:").grid(row=0, column=0, padx=10, pady=10, sticky="e")
entry_search = ttk.Entry(tab_search_contacts, width=50)
entry_search.grid(row=0, column=1, padx=10, pady=10)

btn_search_contact = ttk.Button(tab_search_contacts, text="Search", command=search_contact)
btn_search_contact.grid(row=0, column=2, padx=10, pady=10)

tree_search = ttk.Treeview(tab_search_contacts, columns=("SN", "Name", "Phone", "Email", "Address"), show="headings")
tree_search.heading("SN", text="SN")
tree_search.heading("Name", text="Name")
tree_search.heading("Phone", text="Phone")
tree_search.heading("Email", text="Email")
tree_search.heading("Address", text="Address")
tree_search.grid(row=1, column=0, columnspan=3, padx=10, pady=10, sticky="nsew")

root.mainloop()
