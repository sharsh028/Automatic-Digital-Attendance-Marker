import sqlite3
from tkinter import Tk, Label, Entry, Button, messagebox
import os
from tkinter import *

def login():
    # Get the entered username and password
    username = username_entry.get()
    password = password_entry.get()

    # Connect to the database
    conn = sqlite3.connect('database/database.db')
    c = conn.cursor()

    # Check if the entered username and password match
    c.execute("SELECT * FROM admin WHERE username=? AND password=?", (username, password))
    admin = c.fetchone()

    if admin:
        root.destroy()  # Close the login window
        open_firstpage()  # Open the first page after successful login
    else:
        messagebox.showerror("Error", "Invalid username or password.")

    # Close the connection
    conn.close()


def open_firstpage():
    # Open the first page using the default program
    os.system("python firstpage_gui.py")


def open_signup():
    # Close the login window
    root.destroy()
    # Open the signup file using the default program
    os.system("python signup.py")


# Create the login form
root = Tk()
root.title("A.D.A.M")
root.geometry("300x200")  # Set the window size explicitly
# Set the window icon
root.iconbitmap('image/logo.ico')

# Main label
label1 = Label(root, text="ADMIN LOGIN", font=("times new roman", 20), bg="lightgray",
               fg="black", height=1)
label1.grid(row=0, column=0, columnspan=2, sticky=N + E + W + S, padx=5, pady=5)

# Username label and entry
username_label = Label(root, text="Username:", font=("Arial", 12))
username_label.grid(row=1, column=0, padx=5, pady=5, sticky=E)
username_entry = Entry(root, font=("Arial", 12))
username_entry.grid(row=1, column=1, padx=5, pady=5)

# Password label and entry
password_label = Label(root, text="Password:", font=("Arial", 12))
password_label.grid(row=2, column=0, padx=5, pady=5, sticky=E)
password_entry = Entry(root, show="*", font=("Arial", 12))
password_entry.grid(row=2, column=1, padx=5, pady=5)

# Signup button
signup_button = Button(root, text="Signup", font=("Arial", 13), bg="grey", fg="white", command=open_signup, width=10)
signup_button.grid(row=3, column=0, padx=5, pady=5, sticky=E+W)

# Login button
login_button = Button(root, text="Login", font=("Arial", 13), bg="grey", fg="white", command=login, width=10)
login_button.grid(row=3, column=1, padx=5, pady=5, sticky=E+W)

root.mainloop()
