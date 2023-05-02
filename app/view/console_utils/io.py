import os
import re
import sys
import datetime
import hashlib
from getpass import getpass

from app.exceptions import InputNumberNotInRangeException, UserInputNotAnIntegerException, \
    InputStringNotInRangeException, InputNotAnEmailException
from app.settings import Password
from app.view.console_utils.colors import color_text


# --------- Out functions ---------

def color_print(text, clr):
    """
    Print a string in the console with the selected color.
    :param text: the string to print in console
    :param clr: the color to format
    :return:
    """

    print(color_text(text, clr))


def clear_console():
    """ Clear the console. """

    if os.name == "posix":
        os.system("clear")
    else:
        os.system("cls")


def exit_stime():
    """ Exit safely the program. """

    # TODO: close db connection
    clear_console()
    print("Leaving the Stime platform...")

    sys.exit(0)


# --------- In functions ---------

def int_input(range_min=1, range_max=99, placeholder=None):
    """
    Read input in console and return a float if between range.
    :param range_min: the minimum of the range
    :param range_max: the maximum of the range
    :param placeholder: placeholder to print in console
    :return: user's input (an integer)
    """

    if placeholder:
        print(placeholder, end='')
    user_input = input()

    try:
        integer = int(user_input)
        if range_min <= integer <= range_max:
            return integer
        else:
            raise InputNumberNotInRangeException(integer, range_min, range_max)
    except ValueError:
        raise UserInputNotAnIntegerException(user_input)


def float_input(range_min=0, range_max=999, placeholder=None):
    """
    Read input in console and return a float if between range.
    :param range_min: the minimum of the range
    :param range_max: the maximum of the range
    :param placeholder: placeholder to print in console
    :return: user's input (a float)
    """

    pass


def string_input(min_size=1, max_size=200, placeholder=None):
    """
    Read input in console and return a float if above max character limit.
    :param min_size: the minimum size of the string
    :param max_size: the limit size of the string
    :param placeholder: placeholder to print in console
    :return: user's input (a string)
    """

    if placeholder:
        print(placeholder, end='')
    user_input = input()

    if min_size <= len(user_input) <= max_size:
        return user_input
    else:
        raise InputStringNotInRangeException(user_input, min_size, max_size)


def password_input(placeholder=None):
    """
    Read a secret input in console and return a hashed string.
    :param placeholder: placeholder to print in console
    :return: user input (a string not visible when entering input)
    """

    unhashed_password = getpass(prompt=placeholder)

    if len(unhashed_password) > 0:
        return hashlib.pbkdf2_hmac(
            'sha256',                           # The hash digest algorithm
            unhashed_password.encode('utf-8'),  # Convert the password to bytes
            Password.SALT,                      # Provide the salt
            100_000                             # 100000 iterations
        ).hex()
    else:
        raise InputStringNotInRangeException(unhashed_password, 1, sys.maxsize)


def email_input(placeholder=None):
    """
    Read input in console and return a string being a valid email address.
    :param placeholder: placeholder to print in console
    :return: user input (a string being a valid email address)
    """

    def is_valid_email(email):
        """
        Check if string is a valid email.
        :param email: the email to validate
        :return: true or false
        """
        email_regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'

        return re.fullmatch(email_regex, email)

    if placeholder:
        print(placeholder, end='')
    user_input = input()

    if is_valid_email(user_input):
        return user_input
    else:
        raise InputNotAnEmailException(user_input)


def date_input(placeholder):
    """
    Retrieves the user's date of birth as a string
    :param placeholder: The prompt text for the input
    :return: The date of birth as a character string in the format "YYYY-MM-DD"
    """
    while True:
        date_str = input(placeholder)
        try:
            # Vérifier si la chaîne de caractères est au format "YYYY-MM-DD"
            datetime.datetime.strptime(date_str, '%Y-%m-%d')
            return date_str
        except ValueError:
            print("Please enter a valid date in YYYY-MM-DD format.")
