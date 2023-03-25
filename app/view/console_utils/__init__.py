import os

from app.view.console_utils.colors import END


def color_print(text, clr):
    """ Print a string in the console with the selected color. """

    if hasattr(clr, 'color'):
        print(f"{clr.color}{text}{END.color}")
    else:
        raise Exception("Unknown color selected")


def clear_console():
    """ Clear the console. """

    if os.name == "posix":
        os.system("clear")
    else:
        os.system("cls")


def print_leave():
    """ Clear the console and print leave message. """

    clear_console()
    print("Leaving the Stime platform...")
