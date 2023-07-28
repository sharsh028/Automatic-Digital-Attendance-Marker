from tkinter import *
import os

root = Tk()
root.configure(background="white")
root.title("A.D.A.M")
# Set the window icon
root.iconbitmap('image/logo.ico')
# Function to call other Python files
def c_dataset():
    os.system("python capture_database.py")

def train_d():
    os.system("python training_dataset.py")

def m_attendance():
    os.system("python recognizer.py")

def v_attendance():
    os.system("python viewAttendanceSheet.py")

def d_dataset():
    os.system("python delete_database.py")

def destroy():
    root.destroy()

# Create a frame to hold the buttons
button_frame = Frame(root, bg="white")
button_frame.grid(row=1, column=0, padx=10, pady=10)

# Main label
label1 = Label(root, text="AUTOMATIC DIGITAL ATTENDANCE MARKER", font=("times new roman", 20), bg="lightgray",
               fg="black", height=2)
label1.grid(row=0, column=0, columnspan=2, sticky=N+E+W+S, padx=5, pady=5)

# Buttons
buttons = [
    {"text": "Create Dataset", "row": 0, "column": 0, "bg": "dodgerblue2", "fg": "white", "command": c_dataset},
    {"text": "Train Dataset", "row": 0, "column": 1, "bg": "dodgerblue3", "fg": "white", "command": train_d},
    {"text": "Mark Attendance", "row": 1, "column": 0, "bg": "dodgerblue3", "fg": "white", "command": m_attendance},
    {"text": "View Attendance Sheet", "row": 1, "column": 1, "bg": "dodgerblue4", "fg": "white", "command": v_attendance},
    {"text": "Delete Dataset", "row": 2, "column": 0, "bg": "dodgerblue4", "fg": "white", "command": d_dataset},
    {"text": "Exit", "row": 2, "column": 1, "bg": "grey", "fg": "white", "command": destroy}
]

for button in buttons:
    btn = Button(button_frame, text=button["text"], font=("times new roman", 20), bg=button["bg"],
                 fg=button["fg"], command=button["command"])
    btn.grid(row=button["row"], column=button["column"], padx=10, pady=10, sticky=N+E+W+S)

# To keep the window open until destroyed
root.mainloop()
