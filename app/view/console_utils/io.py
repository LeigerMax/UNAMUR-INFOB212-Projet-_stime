import os

from app.Exceptions import InputIntegerNotInRangeException, UserInputNotAnIntegerException
from app.view.console_utils.colors import END


# --------- Out functions ---------

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


# --------- In functions ---------

def int_input(range_min=1, range_max=99):
    """ Read input in console and return an integer if between range"""

    user_input = input()

    try:
        integer = int(user_input)
        if range_min <= integer <= range_max:
            return integer
        else:
            raise InputIntegerNotInRangeException(integer, range_min, range_max)
    except ValueError:
        raise UserInputNotAnIntegerException(user_input)
