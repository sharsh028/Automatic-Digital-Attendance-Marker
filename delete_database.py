import sqlite3
from tkinter import *
from tkinter import messagebox
import os

conn = sqlite3.connect('database/database.db')
c = conn.cursor()

def validate_login():
    # Get the entered username and password
    username = username_entry.get()
    password = password_entry.get()

    # Check if the username and password match
    c.execute("SELECT * FROM admin WHERE username = ? AND password = ?", (username, password))
    admin = c.fetchone()

    if admin:
        # Username and password are valid
        delete_entry()
    else:
        # Invalid username or password
        messagebox.showerror("Error", "Invalid username or password")

def delete_entry():
    # Get the roll number to delete
    roll_number = uid_val.get()

    # Delete the entry from the database
    c.execute("DELETE FROM students WHERE Roll_number = ?", (roll_number,))
    conn.commit()

    # Delete associated image files
    for file in os.listdir('dataset/'):
        if file.endswith('.jpg') and (roll_number in file):
            os.remove('dataset/' + file)

    messagebox.showinfo("Success", "Entry deleted successfully!")
    root.destroy()

def submit_e():
    validate_login()

root = Tk()
root.title("A.D.A.M")
# Set the window icon
root.iconbitmap('image/logo.ico')

label1 = Label(root, text="DELETE DATABASE ENTRY", font=("times new roman", 20), bg="lightgray", fg="black", height=1)
label1.grid(row=0, column=0, columnspan=2, sticky=N+E+W+S, padx=5, pady=5)

uid = Label(root, text="Enter Roll No:", font=("Arial", 12))
uid_val = Entry(root, font=("Arial", 12))
uid.grid(row=1, column=0, padx=10, pady=10, sticky=E)
uid_val.grid(row=1, column=1, padx=10, pady=10, sticky=W)

username_label = Label(root, text="Username:", font=("Arial", 12))
username_label.grid(row=2, column=0, padx=5, pady=5, sticky=E)
username_entry = Entry(root, font=("Arial", 12))
username_entry.grid(row=2, column=1, padx=5, pady=5)

password_label = Label(root, text="Password:", font=("Arial", 12))
password_label.grid(row=3, column=0, padx=5, pady=5, sticky=E)
password_entry = Entry(root, show="*", font=("Arial", 12))
password_entry.grid(row=3, column=1, padx=5, pady=5)

submit = Button(root, text="Submit", font=("Arial", 12), bg="grey", fg="white", command=submit_e)
submit.grid(row=4, columnspan=2, padx=10, pady=10, sticky=N+E+S+W)

root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
root.rowconfigure(0, weight=1)
root.rowconfigure(1, weight=1)

root.mainloop()

conn.close()
