"""Password Manager

This application allows the user to generate new passwords, and store their new or existing 
passwords as a .txt file.
"""
from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
# Create a window for application.
window = Tk()
window.title("Password Manager")

# Create canvas for window.
canvas = Canvas(width=600, height=500)
# Create PhotoImage in order to use image on canvas.
logo = PhotoImage(file="logo.png")
# Adds logo image to canvas and displays it on the window.
canvas.create_image(300, 100, image=logo)
canvas.pack()

# Create labels for input fields.
website_label = Label(text="Website:")
email_username_label = Label(text="Email/Username:")
password_label = Label(text="Password:")

# Create buttons.
generate_button = Button(text="Generate Password")
add_button = Button(text="Add")


window.mainloop()
