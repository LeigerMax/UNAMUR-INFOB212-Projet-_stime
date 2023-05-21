from app.exceptions import InputNumberNotInRangeException, UserInputNotAnIntegerException
from app.view.console_utils.colors import BLUE
from app.view.console_utils.io import color_print, clear_console, int_input



def item_shop_platform_view(all_objet):
    clear_console()
    color_print("[ITEM PLATFORM MARKET]", BLUE)
    print("| {:<4} | {:<50} | {:<80} | {:<20}| {:<7} |".format("Num", "Name", "Description","Game", "Price"))
    print("+{}+{}+{}+{}+{}+".format("-"*6, "-"*52,"-"*82, "-"*21, "-"*7))

    for i, objet in enumerate(all_objet, start=1):
        print(objet.nom, objet.description,objet.game_id,objet.price)
        print("| {:<4} | {:<50} | {:<80} | {:<20}| {:<7}€ |".format(i, objet.nom, objet.description, objet.game_id, objet.price))


    objet_total = 0

    for objet in all_objet:
        objet_total = objet_total+1

    options = """What do you want to do ?
    Item number you want to see
    0. for leave"""
    print(options)

    try:
        return int_input(0, objet_total, placeholder="Choice: ") #TODO jeu_total not working 
    except (UserInputNotAnIntegerException, InputNumberNotInRangeException):
        return item_shop_platform_view(all_objet)
