import sqlite3
from tkinter import Tk, Label, Entry, Button, messagebox
import os
from tkinter import *

# Connect to the database
conn = sqlite3.connect('database/database.db')
c = conn.cursor()

# Check if the admin table exists
c.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='admin'")
table_exists = c.fetchone()

# If the admin table doesn't exist, create it
if not table_exists:
    c.execute('''
        CREATE TABLE admin (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            username TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL
        )
    ''')

    conn.commit()

# Close the connection
conn.close()

def submit():
    # Get the entered values
    name = name_entry.get()
    username = username_entry.get()
    password = password_entry.get()

    # Connect to the database
    conn = sqlite3.connect('database/database.db')
    c = conn.cursor()

    try:
        # Insert the admin details into the admin table
        c.execute("INSERT INTO admin (name, username, password) VALUES (?, ?, ?)", (name, username, password))
        conn.commit()
        messagebox.showinfo("Success", "Admin details stored successfully!")
        root.destroy()  # Close the signup window
        open_login_file()  # Open the login file
    except sqlite3.IntegrityError:
        messagebox.showerror("Error", "Username already exists. Please choose a different username.")

    # Close the connection
    conn.close()

def open_login_file():
    # Open the login file using the default program
    os.system("python login.py")

# Create the signup form
root = Tk()
root.title("A.D.A.M")
root.geometry("300x200")  # Set the window size explicitly
# Set the window icon
root.iconbitmap('image/logo.ico')

# Main label
label1 = Label(root, text="ADMIN SIGNUP", font=("times new roman", 20), bg="lightgray",
               fg="black", height=1)
label1.grid(row=0, column=0, columnspan=2, sticky=N+E+W+S, padx=5, pady=5)

# Name label and entry
name_label = Label(root, text="Name:", font=("Arial", 12))
name_label.grid(row=1, column=0, padx=5, pady=5, sticky="e")
name_entry = Entry(root, font=("Arial", 12))
name_entry.grid(row=1, column=1, padx=5, pady=5)

# Username label and entry
username_label = Label(root, text="Username:", font=("Arial", 12))
username_label.grid(row=2, column=0, padx=5, pady=5, sticky=E)
username_entry = Entry(root, font=("Arial", 12))
username_entry.grid(row=2, column=1, padx=5, pady=5)

# Password label and entry
password_label = Label(root, text="Password:", font=("Arial", 12))
password_label.grid(row=3, column=0, padx=5, pady=5, sticky=E)
password_entry = Entry(root, show="*", font=("Arial", 12))
password_entry.grid(row=3, column=1, padx=5, pady=5)

# Submit button
submit_button = Button(root, text="Submit", font=("Arial", 13), bg="grey", fg="white", command=submit)
submit_button.grid(row=4, column=0, columnspan=2, padx=5, pady=10)

root.mainloop()
