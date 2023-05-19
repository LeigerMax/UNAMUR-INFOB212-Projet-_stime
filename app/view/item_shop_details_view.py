from app.exceptions import InputNumberNotInRangeException, UserInputNotAnIntegerException
from app.view.console_utils.colors import BLUE
from app.view.console_utils.io import color_print, clear_console, int_input



def item_shop_details_view(objet):
    clear_console()
    color_print("[ITEM DETAILS]", BLUE)
    print("\nName : " + objet.nom)
    print("Description : " + objet.description)
    print("Price : " + str(objet.price) + " €")

    print("\nDo you wish to buy this item ?")
    print("0. Yes")
    print("1. No")

    try:
        return int_input(0, 1, placeholder="Choice: ") #TODO jeu_total not working 
    except (UserInputNotAnIntegerException, InputNumberNotInRangeException):
        return item_shop_details_view(objet)

