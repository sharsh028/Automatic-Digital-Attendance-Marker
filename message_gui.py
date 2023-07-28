from tkinter import *

root = Tk()
root.title("Message")
root.geometry("300x150")
# Set the window icon
root.iconbitmap('image/logo.ico')

# Configure the main frame
main_frame = Frame(root, bg="white")
main_frame.pack(fill="both", expand=True)

# Create a label
message = Label(main_frame, text="Successfully Done! :)", font=("Arial", 18),  fg="black")
message.pack(pady=(30, 10))

# Create a button
submit = Button(main_frame, text="Message Received", font=("Arial", 16), bg="grey", fg="white", bd=0, padx=20, pady=10, activebackground="grey", activeforeground="white", relief="groove", command=root.destroy)
submit.pack(pady=(0, 30))

# Set the background color of the main frame
root.configure(bg="grey")

# Main loop
root.mainloop()
