from app.exceptions import InputStringNotInRangeException
from app.view.console_utils.colors import BLUE, RED_BLD
from app.view.console_utils.io import clear_console, color_print, string_input, password_input


def login_menu(error_message=None):
    """ Show login menu, then return user inputs. """

    clear_console()
    color_print("[LOGIN]", BLUE)
    if error_message:
        color_print(error_message, RED_BLD)

    try:
        username = string_input(placeholder="Username: ")
        password = password_input(placeholder="Password: ")
    except InputStringNotInRangeException:
        return login_menu("Username or password does not respect size limit")

    return {
        "username": username,
        "password": password
    }


    #show_menu()

    ## produire le SQL query en dessous
    ##IF login OK -> show_menu()