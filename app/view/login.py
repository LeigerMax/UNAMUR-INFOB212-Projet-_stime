from app.view.console_utils.colors import BLUE
from app.view.console_utils.io import clear_console, color_print, string_input, password_input


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