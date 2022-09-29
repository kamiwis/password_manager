"""Password Manager

This application allows the user to generate new passwords, and store their new or existing 
passwords as a .txt file.

To personalize the file, you can uncomment the EMAIL constant variable, save your email address
to is as a string. Next, uncomment line 77 - under the comment '# Uncomment following row if you
would like a constant EMAIL to be populated in Email/Username'

This application utilizes the `tkinter` module, `messagebox` from `tkinter`, 'pyperclip' and 
`password_generator` module.
"""
from tkinter import *
from tkinter import messagebox
from password_generator import password_generator
import pyperclip

# Uncomment EMAIL constant and change to your email if you would like to autopopulate your email
#EMAIL = ""


def generate_password():
    """Calls password_generator from password_generator module. Generates new randomly
    generated password and inserts it into the password Entry field."""
    if len(password.get()) == 0:
        password.insert(0, password_generator())
        # Copy password to clipboard.
        pyperclip.copy(password.get())

def save_password():
    """Saves the current information to data.txt."""
    # Ask user if the information entered is correct to ensure they want to save.
    is_correct = messagebox.askokcancel(title=website, message=f"Saving these details:\nEmail: "
    f"{email_username.get()}\nPassword: {password.get()}\nWebsite: {website.get()}\n OK to save?")
    # Save information to file.
    if is_correct:
        with open("data.txt", "a") as f:
            f.write(
                f"{website.get()} | {email_username.get()} | {password.get()}\n")
        website.delete(0, END)
        password.delete(0, END)

def complete_input():
    """Checks that all input fields have been completed before saving."""
    if len(website.get()) == 0 or len(password.get()) == 0:
        messagebox.showinfo(title="Oops", message="Please complete all fields")
    else:
        save_password()

# Create a window for application interface.
window = Tk()
window.title("Password Manager")
# Sets padding to 50 on both x and y axis.
window.config(padx=50, pady=50)

# Create canvas for window.
canvas = Canvas(width=200, height=200)
# Create PhotoImage in order to use image on canvas.
logo = PhotoImage(file="logo.png")
# Adds logo image to canvas and displays it in the center of the canvas.
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
website.focus()
email_username = Entry(width=35)
email_username.grid(row=2, column=1, columnspan=2)
# Uncomment following row if you would like a constant EMAIL to be populated in Email/Username
#email_username.insert(0, EMAIL)
password = Entry(width=18)
password.grid(row=3, column=1)

# Create buttons and place in grid.
generate_button = Button(text="Generate Password", command=generate_password)
generate_button.grid(row=3, column=2)
add_button = Button(text="Add", width=36, command=complete_input)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
