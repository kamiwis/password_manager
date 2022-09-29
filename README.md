# password_manager
This app is a Password Manager that allows the user to generate a new random password or input their
own, input the website this password is for, and their email/username used for this website. It will
then save this information to a .txt file, allowing the user to store their passwords in a secure
place.

# Motivation
With the number of websites we all subscribe to, it's important to store your passwords for future
use. It is also imporant to create secure passwords for all of your accounts instead of reusing the
same password. This program allows the user to generate secure passwords with the click of a button
and will save the password information locally. Not everyone is comfortable using a password manager
like Last Pass. Using this password manager stores your passwords locally.

# Installation
To install locally, fork a copy of this repository and save locally to your computer. Ensure that
your Python interpreter has `pyperclip` installed. 

To personalize this program, uncomment the EMAIL constant variable on line 19, save your email
address to EMAIL as a string. Next, uncomment line 77 - under the comment '# Uncomment following
row if you would like a constant EMAIL to be populated in Email/Username'. This will autopopulate
your email address in the email/username field.


# How to use
Inside the working directory containing all the files, run `python3 main.py`.
This will bring up a GUI with the Password Manager app.
Under Website, insert the name of the website the password will be used for. 
Under Email/Username, insert the email used for the account.
Under password, either input a password you are already using, or click `Generate Password` to 
generate a random secure password. This will autopopulate the new password in the password field
and will automatically copy the password to your clipboard so you can use it on the website.  
