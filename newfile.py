from tkinter import *
from tkinter import messagebox

# add a new contact
def add_contact():
    name = name_entry.get()
    phone = phone_entry.get()
    email = email_entry.get()

    if name and phone and email:
        contacts.append({"name": name, "phone": phone, "email": email})
        update_contact_listbox()
        clear_entries()
        save_contacts_to_file()
    else:
        messagebox.showwarning("Input Error", "All fields are required.")

# update the contact listbox
def update_contact_listbox():
    contact_listbox.delete(0, END)
    for contact in contacts:
        contact_listbox.insert(END, contact["name"])

# view a contact's details
def view_contact(event):
    selected_index = contact_listbox.curselection()
    if selected_index:
        selected_contact = contacts[selected_index[0]]
        fill_entries(selected_contact)

# edit a selected contact
def edit_contact():
    selected_index = contact_listbox.curselection()
    if selected_index:
        contacts[selected_index[0]] = {"name": name_entry.get(), "phone": phone_entry.get(), "email": email_entry.get()}
        update_contact_listbox()
        save_contacts_to_file()

# delete a selected contact
def delete_contact():
    selected_index = contact_listbox.curselection()
    if selected_index:
        contacts.pop(selected_index[0])
        update_contact_listbox()
        save_contacts_to_file()

# save contacts to a file
def save_contacts_to_file():
    with open("contacts.txt", "w") as file:
        for contact in contacts:
            file.write(f"{contact['name']}|{contact['phone']}|{contact['email']}\n")

# load contacts from a file
def load_contacts_from_file():
    contacts = []
    try:
        with open("contacts.txt", "r") as file:
            for line in file:
                name, phone, email = line.strip().split("|")
                contacts.append({"name": name, "phone": phone, "email": email})
    except FileNotFoundError:
        pass 
    return contacts

# clear all entry fields
def clear_entries():
    name_entry.delete(0, END)
    phone_entry.delete(0, END)
    email_entry.delete(0, END)

# selected contact details
def fill_entries(contact):
    clear_entries()
    name_entry.insert(END, contact["name"])
    phone_entry.insert(END, contact["phone"])
    email_entry.insert(END, contact["email"])

# save contacts to file
def save_contacts():
    save_contacts_to_file()
    messagebox.showinfo("Save Contacts", "Contacts saved successfully!")

# main window
root = Tk()
root.title("Contact Management System")
root.geometry("400x400")
root.resizable(False, False)

# Variables
contacts = load_contacts_from_file()

# contact details
Label(root, text="Name:", font="lucida 12").pack(pady=5)
name_entry = Entry(root, font="lucida 12")
name_entry.pack(pady=5)

Label(root, text="Phone:", font="lucida 12").pack(pady=5)
phone_entry = Entry(root, font="lucida 12")
phone_entry.pack(pady=5)

Label(root, text="Email:", font="lucida 12").pack(pady=5)
email_entry = Entry(root, font="lucida 12")
email_entry.pack(pady=5)

# contact
Button(root, text="Add Contact", command=add_contact, font="lucida 12").pack(pady=10)
Button(root, text="Edit Contact", command=edit_contact, font="lucida 12").pack(pady=10)
Button(root, text="Delete Contact", command=delete_contact, font="lucida 12").pack(pady=10)
Button(root, text="Save Contacts", command=save_contacts, font="lucida 12").pack(pady=10)

# display contacts
contact_listbox = Listbox(root, font="lucida 12")
contact_listbox.pack(pady=10, fill=BOTH, expand=True)
contact_listbox.bind("<<ListboxSelect>>", view_contact)

# listbox
update_contact_listbox()

# main loop
root.mainloop()


