from app.exceptions import InputStringNotInRangeException, InputNotAnEmailException
from app.view.console_utils.io import clear_console, color_print, string_input, password_input, email_input, date_input
from app.view.console_utils.colors import BLUE, RED_BLD

import datetime

def login_view(error_message=None):
    """ Show login menu, then return user inputs. """

    clear_console()
    color_print("[LOGIN]", BLUE)
    if error_message:
        color_print(error_message, RED_BLD)

    try:
        username = string_input(placeholder="Username: ")
        password = password_input(placeholder="Password: ", with_clear=True)
    except InputStringNotInRangeException:
        return login_view("Username or password does not respect size limit")

    return {
        "username": username,
        "password": password[0],
        "password_clear": password[1]
    }


def register_view(error_message=None):
    """
    Show register form, then return user inputs.
    :param error_message: a message to display
    :return: the option selected
    """

    clear_console()
    color_print("[REGISTER]", BLUE)
    if error_message:
        color_print(error_message, RED_BLD)

    print("Please enter the following information:")

    try:
        username = string_input(placeholder="New username: ")
        password = password_input(placeholder="Your password: ", with_clear=True)
        password_confirm = password_input(placeholder="Confirm password: ")
        firstname = string_input(placeholder="Your firstname: ")
        lastname = string_input(placeholder="Your lastname: ")
        email = email_input(placeholder="Your email address: ")
        date_of_birth = date_input(placeholder="Your date of birth (YYYY-MM-DD): ") 
    except InputStringNotInRangeException:
        return register_view("One or many fields do not respect size limit")
    except InputNotAnEmailException:
        return register_view("Email is not valid")

    return {
        "username": username,
        "password": password[0],
        "confirm_password": password_confirm,
        "password_clear": password[1],
        "firstname": firstname,
        "lastname": lastname,
        "email": email,
        "date_of_birth": date_of_birth
    }
