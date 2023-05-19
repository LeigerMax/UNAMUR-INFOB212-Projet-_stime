from app.exceptions import InputNumberNotInRangeException, UserInputNotAnIntegerException
from app.view.console_utils.colors import BLUE, RED
from app.view.console_utils.io import color_print, clear_console, int_input



def item_shop_details_view_user(objet, originalObjet, money, price):
    clear_console()
    color_print("[ITEM DETAILS]", BLUE)
    print("\nName : " + originalObjet.nom)
    print("Description : " + originalObjet.description)
    print("Price : " + str(price) + " €")
    print("Actual possessor :" + str(objet.possesseur))
    print("\nDo you wish to buy this item ?")
    print("0. Yes")
    print("1. No")

    if money == 1:
        color_print("YOU DO NOT HAVE THE MONEY TO BUY IT", RED)

    try:
        return int_input(0, 1, placeholder="Choice: ") #TODO jeu_total not working 
    except (UserInputNotAnIntegerException, InputNumberNotInRangeException):
        return item_shop_details_view_user(objet, originalObjet, money, price)

