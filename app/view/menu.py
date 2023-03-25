from app.Exceptions import UserInputNotAnIntegerException, InputNumberNotInRangeException
from app.view.console_utils.io import clear_console, color_print, int_input, string_input, password_input
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
    What do you wish to do ? Enter the number you wish for :
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
        return login_register_menu("/!\\ Invalid input /!\\")

    # match choice1:
    #     case 1:
    #         register()
    #     case 2:
    #         login()
    #     case 3:
    #         leave()


def login_menu(error_message=None):
    """ Show login menu, then return user inputs. """

    clear_console()
    color_print("[LOGIN]", BLUE)
    print("Please enter the following information:")

    username = string_input(placeholder="Username: ")
    password = password_input(placeholder="Password: ")
    password_confirm = password_input(placeholder="Password (confirm): ")

    return {
        "username": username,
        "password": password,
        "password_confirm": password_confirm
    }


    #show_menu()

    ## produire le SQL query en dessous
    ##IF login OK -> show_menu()