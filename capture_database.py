import sqlite3
import cv2
import os
from tkinter import *
from tkinter.ttk import *


def assure_path_exists(path):
    dir = os.path.dirname(path)
    if not os.path.exists(dir):
        os.makedirs(dir)


# Check if the database file exists
if not os.path.exists('database/database.db'):
    # Run the sql.py file to create the database
    os.system("python sql.py")

# Create the database connection
conn = sqlite3.connect('database/database.db')
c = conn.cursor()

# Fetch courses, branches, and years from the offline database
c.execute("SELECT course_name FROM courses")
course_options = ["None"] + [row[0] for row in c.fetchall()]

c.execute("SELECT branch_name FROM branch")
branch_options = ["None"] + [row[0] for row in c.fetchall()]

c.execute("SELECT value FROM year")
year_options = ["None"] + [row[0] for row in c.fetchall()]

# Global variables to store input values
val1 = ""
val3 = ""
val4 = ""
val5 = ""


def submit_e():
    global val1, val3, val4, val5
    val1 = uid_val.get()
    val2 = name_val.get()
    val3 = selected_course.get()
    val4 = selected_branch.get()
    val5 = selected_year.get()

    face_id = str(val1)
    name = str(val2)
    crs = str(val3)
    br = str(val4)
    yr = str(val5)
    c.execute("INSERT INTO students(Roll_number,Name,course_id,branch_id,year_id) VALUES(?,?,?,?,?)",
              (face_id, name, crs, br, yr))
    conn.commit()
    root.destroy()

    # Start capturing Video
    vid_cam = cv2.VideoCapture(0)

    # Detect object in video stream using Haarcascade Frontal Face
    face_detector = cv2.CascadeClassifier('cascades/haarcascade_frontalface_default.xml')

    # Initialize count variable to count scanned images
    count = 0
    assure_path_exists("dataset/")

    # Start scanning loop
    while True:
        # Capture video frame
        _, image_frame = vid_cam.read()
        cv2.imshow('frame', image_frame)

        # Convert frame to grayscale
        gray = cv2.cvtColor(image_frame, cv2.COLOR_BGR2GRAY)

        # Detect frames of different sizes, list of faces rectangles
        faces = face_detector.detectMultiScale(gray, 1.3, 5)

        # Loop for each face
        for (x, y, w, h) in faces:
            # Crop the image frame into rectangle
            cv2.rectangle(image_frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
            # Increment count
            count += 1

            # Save the captured image into datasets folder
            cv2.imwrite("dataset/User." + str(face_id) + '.' + str(count) + ".jpg", gray[y:y + h, x:x + w])

            # Display the video frame, with bounded rectangle on image frame
            cv2.imshow('frame', image_frame)

        # To stop scanning images, press 'q' for at least 100ms
        if cv2.waitKey(100) & 0xFF == ord('q'):
            break
        elif count >= 30:
            os.system("python message_gui.py")
            break

    # Stop video
    vid_cam.release()

    # Close all started windows
    cv2.destroyAllWindows()

    conn.close()


# Create the main window
root = Tk()
root.title("A.D.A.M")
# Set the window icon
root.iconbitmap('image/logo.ico')

# Main label
label1 = Label(root, text="CREATING DATABASE ENTRY", font=("times new roman", 20), background="lightgray",
               foreground="black")
label1.grid(row=0, column=0, columnspan=2, sticky=N + E + W + S, padx=5, pady=5)

# Label and entry for Roll No
uid = Label(root, text="Roll No:", font=("Arial", 12))
uid_val = Entry(root, font=("Arial", 12))
uid.grid(row=1, column=0, padx=5, pady=5, sticky=E)
uid_val.grid(row=1, column=1, padx=5, pady=5, sticky=W)

# Label and entry for Full Name
name = Label(root, text="Full Name:", font=("Arial", 12))
name_val = Entry(root, font=("Arial", 12))
name.grid(row=2, column=0, padx=5, pady=5, sticky=E)
name_val.grid(row=2, column=1, padx=5, pady=5, sticky=W)

# Label and dropdown menu for Course selection
course_label = Label(root, text="Course:", font=("Arial", 12))
selected_course = StringVar(root)
selected_course.set(course_options[0])
course_menu = OptionMenu(root, selected_course, *course_options)
course_label.grid(row=3, column=0, padx=5, pady=5, sticky=E)
course_menu.grid(row=3, column=1, padx=5, pady=5, sticky=W)

# Label and dropdown menu for Branch selection
branch_label = Label(root, text="Branch:", font=("Arial", 12))
selected_branch = StringVar(root)
selected_branch.set(branch_options[0])
branch_menu = OptionMenu(root, selected_branch, *branch_options)
branch_label.grid(row=4, column=0, padx=5, pady=5, sticky=E)
branch_menu.grid(row=4, column=1, padx=5, pady=5, sticky=W)


# Label and dropdown menu for Year selection
year_label = Label(root, text="Year:", font=("Arial", 12))
selected_year = StringVar(root)
selected_year.set(year_options[0])
year_menu = OptionMenu(root, selected_year, *year_options)
year_label.grid(row=5, column=0, padx=5, pady=5, sticky=E)
year_menu.grid(row=5, column=1, padx=5, pady=5, sticky=W)

# Styling for the Submit button
submit = Button(root, text="Submit", command=submit_e)
submit.grid(row=6, column=0, columnspan=2, padx=5, pady=5, sticky=N + E + S + W)

root.mainloop()
