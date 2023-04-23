from app.view.console_utils.colors import BLUE
from app.view.console_utils.io import color_print, clear_console, int_input
from app.exceptions import UserInputNotAnIntegerException, InputNumberNotInRangeException
import time

def shop_panier_bought_view(panier):
    clear_console()
    color_print("[BOUGHT]", BLUE)

    #Demande si c'est à livrer
    options = """
    Do you want the product to be delivered ?
    1.  Yes
    2.  No
        """

    print(options)
    try:
        is_delivery = int_input(1, 2, placeholder="Choice: ")
    except (UserInputNotAnIntegerException, InputNumberNotInRangeException):
        return shop_panier_bought_view(panier)

    #Choix du moyen de paiement
    options = """
    Choose the payment method
    1.  Card
    2.  Wallet
    3.  Leave
        """

    print(options)
    try:
        means_of_payment = int_input(1, 3, placeholder="Choice: ")
    except (UserInputNotAnIntegerException, InputNumberNotInRangeException):
        return shop_panier_bought_view(panier)
    
    return is_delivery, means_of_payment

def card_view(panier,is_livraison):
    clear_console()
    color_print("[CARD]", BLUE)
    print("You choose card for purchase")

    print("Ongoing treatment ... wait ...") #On n'implémente pas le payment par carte
    time.sleep(3)

    shop_panier_bought_sucess_view()

    
def wallet_view(panier,is_livraison):
    clear_console()
    color_print("[Wallet]", BLUE)
    print("You choose wallet for purchase")

    #TODO: Pas assez redirection vers card_view

def shop_panier_bought_sucess_view():
    print("Congratulations ! You have purchased the products in your cast")
    print("\nPress enter to continue...")