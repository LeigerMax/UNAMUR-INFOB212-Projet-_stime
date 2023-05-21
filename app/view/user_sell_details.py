from app.exceptions import InputNumberNotInRangeException, UserInputNotAnIntegerException
from app.view.console_utils.colors import BLUE, GREEN
from app.view.console_utils.io import clear_console, color_print, int_input


def user_sell_details_view(username):
    clear_console()
    
    print("How much do you wish to sell this item ? (between 0 and 2000)")

    try:
        return int_input(0, 2000, placeholder="Choice: ") #TODO jeu_total not working 
    except (UserInputNotAnIntegerException, InputNumberNotInRangeException):
        return user_sell_details_view(username, myObjects, originalsObjects)