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
window.config(padx=50, pady=50)

# Create canvas for window.
canvas = Canvas(width=200, height=200)
# Create PhotoImage in order to use image on canvas.
logo = PhotoImage(file="logo.png")
# Adds logo image to canvas and displays it on the window.
canvas.create_image(100, 100, image=logo)
canvas.grid(row=0, column=1)

# Create labels for input fields and place in grid.
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
email_username_label = Label(text="Email/Username:")
email_username_label.grid(row=2, column=0)
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

# Create input fields and place in grid.
website = Entry(width=35)
website.grid(row=1, column=1, columnspan=2)
email_username = Entry(width=35)
email_username.grid(row=2, column=1, columnspan=2)
password = Entry(width=18)
password.grid(row=3, column=1)

# Create buttons and place in grid.
generate_button = Button(text="Generate Password")
generate_button.grid(row=3, column=2)
add_button = Button(text="Add", width=36)
add_button.grid(row=4, column=1, columnspan=2)




window.mainloop()
