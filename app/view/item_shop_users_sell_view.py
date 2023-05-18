from app.exceptions import InputNumberNotInRangeException, UserInputNotAnIntegerException
from app.view.console_utils.colors import BLUE, GREEN
from app.view.console_utils.io import clear_console, color_print, int_input


def item_shop_users_sell_view(username, myObjects, originalsObjects):
    clear_console()
    color_print("[YOUR ITEMS]", BLUE)
    number = 0 
    for i, objet in enumerate(originalsObjects):
        color_print(f"{i+1} - {objet.nom} - {objet.description}", GREEN)
        number += 1
    print("\nWhich one dou you wish to sell ?.")
    print("Press '0' to exit")

    try:
        return int_input(0, number, placeholder="Choice: ") #TODO jeu_total not working 
    except (UserInputNotAnIntegerException, InputNumberNotInRangeException):
        return item_shop_users_sell_view(username, myObjects, originalsObjects)