from app.exceptions import InputNumberNotInRangeException, UserInputNotAnIntegerException
from app.view.console_utils.colors import BLUE
from app.view.console_utils.io import color_print, clear_console, int_input



def item_shop_view():
    clear_console()
    color_print("[ITEM MARKET]", BLUE)
    print("\nWhich market do you wish to access to ?")
    print("1. Stime item market ")
    print("2. User item market")
    print("3. Exit\n")


    try:
        return int_input(0, 3, placeholder="Choice: ") #TODO jeu_total not working 
    except (UserInputNotAnIntegerException, InputNumberNotInRangeException):
        return item_shop_view()
