from app.exceptions import UserInputNotAnIntegerException, InputNumberNotInRangeException
from app.view.console_utils.io import clear_console, color_print, int_input
from app.view.console_utils.colors import BLUE, RED_BLD


def login_register_menu(error_message=None):
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
        return login_register_menu("Invalid input")

    # match choice1:
    #     case 1:
    #         register()
    #     case 2:
    #         login()
    #     case 3:
    #         leave()
