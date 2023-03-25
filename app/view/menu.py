from app.Exceptions import UserInputNotAnIntegerException, InputIntegerNotInRangeException
from app.view.console_utils.io import clear_console, color_print, int_input
from app.view.console_utils.colors import BLUE


def login_register_menu():
    """ Show login and register menu to console, then return user choice. """

    header = """
    ********************************************
    *                                          *
    *       Welcome to the Stime platform!     *
    *                                          *
    ********************************************
    """

    options = """
    What do you wish to do ? Enter the number you wish for :
    1.  Register
    2.  Login
    3.  Leave
    """

    clear_console()
    color_print(header, BLUE)
    print(options)

    try:
        return int_input(1, 3)
    except (UserInputNotAnIntegerException, InputIntegerNotInRangeException):
        return login_register_menu()

    # match choice1:
    #     case 1:
    #         register()
    #     case 2:
    #         login()
    #     case 3:
    #         leave()
