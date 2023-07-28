from tkinter import *
import os

root = Tk()
root.title("A.D.A.M")
# Set the window icon
root.iconbitmap('image/logo.ico')

# Function to open Excel file
def open_excel(file_path):
    os.system(f'start excel "{file_path}"')

# Function to open the Attendance_Report folder
def open_folder():
    os.system("python report.py")  # Execute report.py file
    folder_path = "Attendance_Report"
    os.startfile(folder_path)  # Open Attendance_Report folder

# Main label
label1 = Label(root, text="ATTENDENCE SHEET", font=("times new roman", 20), bg="lightgray",
               fg="black", height=1)
label1.grid(row=0, column=0, columnspan=2, sticky=N+E+W+S, padx=5, pady=5)

# Button click handlers
def open_file1():
    open_excel("Attendance_Files/Btech_CS_4th/KHU-801.xlsx")

def open_file2():
    open_excel("Attendance_Files/Btech_CS_4th/KOE-083.xlsx")

def open_file3():
    open_excel("Attendance_Files/Btech_CS_4th/KOE-094.xlsx")

# Create buttons with gray background
button1 = Button(root, text="Rural Development: Administration and Planning", command=open_file1, bg="gray", width=40, height=3)
button2 = Button(root, text="Entrepreneurship Development", command=open_file2, bg="gray", width=40, height=3)
button3 = Button(root, text="Digital and Social Media Marketing", command=open_file3, bg="gray", width=40, height=3)
button4 = Button(root, text="Generate And View Report", command=open_folder, bg="gray", width=40, height=3)

# Grid layout for buttons
button1.grid(row=1, column=0, padx=10, pady=10)
button2.grid(row=1, column=1, padx=10, pady=10)
button3.grid(row=2, column=0, padx=10, pady=10)
button4.grid(row=2, column=1, padx=10, pady=10)

# Configure window background color
root.configure(bg="white")

root.mainloop()
