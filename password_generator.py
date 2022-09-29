"""Password Generator module for Password Manager.

This module returns a randomly generated password consisting of: 8-10 letters, 2-4 symbols,
and 2-4 numbers that are shuffled at random. This module was created to be used with the Password
Manager app.

Example Output:
    "PM6KG5Nz0+%&0zukR"
    "Z*Y90*(CgOuNX&"

Attributes:
    letters (list): list of (str) containing all letters that can be included in the new password.
    numbers (list): list of (int) containing numbers from 0 - 9.
    symboles (list): list of (str) containing all symbols that can be included in password.

This file can be imported as a module and contains the following functions:
    *password_generator() - Generates a password with random letters, numbers, and symbols.
"""
from random import choice, randint, shuffle

letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
    'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
    'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


def password_generator():
    """Generates a password with random letters, numbers, and symbols."""
    password_letters = [choice(letters) for i in range(randint(8, 10))]
    password_symbols = [choice(symbols) for j in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    password = password_letters + password_symbols + password_numbers
    shuffle(password)

    return "".join(password)
