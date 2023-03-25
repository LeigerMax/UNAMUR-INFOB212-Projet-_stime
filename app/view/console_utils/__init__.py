import os


class ConsoleColor:
    def __init__(self, color):
        self.color = color


class Colors:
    """ Class containing all colors printable for the console. """
    END = ConsoleColor('\33[0m')

    BOLD = ConsoleColor('\33[1m')
    ITALIC = ConsoleColor('\33[3m')
    UNDERLINE = ConsoleColor('\033[4m')

    BLACK = ConsoleColor('\33[30m')
    RED = ConsoleColor('\33[31m')
    GREEN = ConsoleColor('\33[32m')
    YELLOW = ConsoleColor('\33[33m')
    BLUE = ConsoleColor('\33[34m')
    VIOLET = ConsoleColor('\33[35m')
    CYAN = ConsoleColor('\33[36m')
    WHITE = ConsoleColor('\33[37m')

    BLACK_BG = ConsoleColor('\33[40m')
    RED_BG = ConsoleColor('\33[41m')
    GREEN_BG = ConsoleColor('\33[42m')
    YELLOW_BG = ConsoleColor('\33[43m')
    BLUE_BG = ConsoleColor('\33[44m')
    VIOLET_BG = ConsoleColor('\33[45m')
    CYAN_BG = ConsoleColor('\33[46m')
    WHITE_BG = ConsoleColor('\33[47m')

    GREY = ConsoleColor('\33[90m')
    RED_BLD = ConsoleColor('\33[91m')
    GREEN_BLD = ConsoleColor('\33[92m')
    YELLOW_BLD = ConsoleColor('\33[93m')
    BLUE_BLD = ConsoleColor('\33[94m')
    VIOLET_BLD = ConsoleColor('\33[95m')
    CYAN_BLD = ConsoleColor('\33[96m')
    WHITE_BLD = ConsoleColor('\33[97m')


def color_print(text, clr):
    """ Print a string in the console with the selected color. """

    if hasattr(clr, 'color'):
        print(f"{clr.color}{text}{Colors.END.color}")
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
