from app.exceptions import InputNumberNotInRangeException, UserInputNotAnIntegerException
from app.model.objet import Objet
from app.model.objet_instance import ObjetInstance
from app.view.console_utils.colors import BLUE
from app.view.console_utils.io import color_print, clear_console, int_input



def item_shop_users_view(all_objet):
    clear_console()
    color_print("[ITEM USERS MARKET]", BLUE)
    print("| {:<4}| {:<12}| {:<20} | {:<50} | {:<80} | {:<20}| {:<7} |".format("Num" ,"SellingDate", "Seller", "Name", "Description","Game", "Price"))
    print("+{}+{}+{}+{}+{}+{}+{}+".format("-"*6,"-"*12,"-"*20, "-"*52,"-"*82, "-"*21, "-"*7))

    for i, transaction in enumerate(all_objet, start=1):
        instance = ObjetInstance.select(transaction.objet)
        objet = Objet.select(instance.objet)
        print("| {:<4} | {:<12}| {:<20} | {:<50} | {:<80} | {:<20}| {:<7}€ |".format(i, transaction.date_mise_en_vente, transaction.revendeur,objet.nom,objet.description, objet.game_id, transaction.prix_vente))

    objet_total = 0

    for objet in all_objet:
        objet_total = objet_total+1


    options = """
    What do you want to do ?
    Item number you want to buy 
    0. for leave
    """
    print(options)

    try:
        return int_input(0, objet_total, placeholder="Choice: ") #TODO jeu_total not working 
    except (UserInputNotAnIntegerException, InputNumberNotInRangeException):
        return item_shop_users_view(all_objet)
