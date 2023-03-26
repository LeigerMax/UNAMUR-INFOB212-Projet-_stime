from app.exceptions import UserInputNotAnIntegerException, InputNumberNotInRangeException
from app.view.console_utils.io import clear_console, color_print, int_input
from app.view.console_utils.colors import BLUE, RED_BLD


def welcome_menu_view(error_message=None):
    """
    Show login and register menu to console, then return user choice.
    :param error_message: a message to display
    :return: the option selected
    """

    header = """
********************************************
*                                          *
*       Welcome to the Stime platform!     *
*                                          *
********************************************
    """

    options = """
What do you want to do ?
1.  Register
2.  Login
3.  Leave
    """

    clear_console()
    color_print(header, BLUE)
    print(options)
    if error_message:
        color_print(error_message, RED_BLD)

    try:
        return int_input(1, 3, placeholder="Choice: ")
    except (UserInputNotAnIntegerException, InputNumberNotInRangeException):
        return welcome_menu_view("Invalid input")


def main_menu_view(username, error_message=None):
    """
    Show main menu when connected, then return user choice.
    :param username: name of the connected user.
    :param error_message: a message to display
    :return: the option selected
    """

    welcome_msg = f"Welcome {username} !"

    options = """
What do you want to do ?
1.  See my games
2.  Buy a game
3.  Buy / sell an item
4.  See my items
5.  Leave
    """

    clear_console()
    color_print(welcome_msg, BLUE)
    print(options)
    if error_message:
        color_print(error_message, RED_BLD)

    try:
        return int_input(1, 5, placeholder="Choice: ")
    except (UserInputNotAnIntegerException, InputNumberNotInRangeException):
        return main_menu_view(username, "Invalid input")
