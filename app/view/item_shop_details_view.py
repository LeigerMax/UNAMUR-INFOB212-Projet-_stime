from app.exceptions import InputNumberNotInRangeException, UserInputNotAnIntegerException
from app.view.console_utils.colors import BLUE
from app.view.console_utils.io import color_print, clear_console, int_input



def item_shop_details_view():
    clear_console()
    color_print("[ITEM DETAILS]", BLUE)
    print("\nWhich item do you wish to buy ?")

