"""Password Manager

This application allows the user to generate new passwords, and store their new or existing 
passwords as a .txt file.

To personalize the file, you can uncomment the EMAIL constant variable, save your email address
to is as a string. Next, uncomment line 77 - under the comment '# Uncomment following row if you
would like a constant EMAIL to be populated in Email/Username'

This script requires that `pyperclip` be installed within the Python environment you are 
running this script in.
"""
from tkinter import *
from tkinter import messagebox
import json
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
    # Save information to file.
    website_data = website.get()
    email_data = email_username.get()
    password_data = password.get()
    new_data = {
        website_data: {
            "email": email_data,
            "password": password_data
        }
    }

    if len(website.get()) == 0 or len(password.get()) == 0:
        messagebox.showinfo(title="Oops", message="Please complete all fields")
    else:
        try:
            with open("data.json", "r") as f:
                # Read existing data.
                data = json.load(f)
        except FileNotFoundError:
            with open("data.json", "w") as f:
                json.dump(new_data, f, indent=4)
        else:
            # Update existing data with new data.
            data.update(new_data)

            with open("data.json", "w") as f:
                # Save updated data to file.
                json.dump(data, f, indent=4)
        finally:
            website.delete(0, END)
            password.delete(0, END)
    
def retrieve_data():
    website_to_find = website.get()
    try:
        # Open json file
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found")
    else:
        if website_to_find in data:
            email_data = data[website_to_find]["email"]
            password_data = data[website_to_find]["password"]
            messagebox.showinfo(title=website_to_find, message=f"Email: {email_data} \nPassword: {password_data}")
        else:
            messagebox.showinfo(title="Error", message=f"No details found for {website_to_find}")

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
website = Entry(width=18)
website.grid(row=1, column=1)
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
add_button = Button(text="Add", width=36, command=save_password)
add_button.grid(row=4, column=1, columnspan=2)
search_button = Button(text="Search", width=13, command=retrieve_data)
search_button.grid(row=1, column=2)

window.mainloop()
