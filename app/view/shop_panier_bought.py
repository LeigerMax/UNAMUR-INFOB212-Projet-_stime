from app.view.console_utils.colors import BLUE,GREEN,RED
from app.view.console_utils.io import color_print, clear_console, int_input,string_input
from app.exceptions import UserInputNotAnIntegerException, InputNumberNotInRangeException,InputStringNotInRangeException
import time

def shop_panier_bought_view(panier):
    clear_console()
    color_print("[BOUGHT]", BLUE)

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
    
    return means_of_payment


def card_view(panier,means_of_payment_data):
    clear_console()
    color_print("[CARD]", BLUE)
    print("You choose card for purchase")
    
    print("What means of payment?")
    for i in range(len(means_of_payment_data)):
        means_of_payment = means_of_payment_data[i]
        print(i,". ", means_of_payment.nom, " avec ", means_of_payment.taxe_du_moyen, "€ de taxe")

    try:
        choice = int_input(0, len(means_of_payment_data)-1, placeholder="Choice: ")
    except (UserInputNotAnIntegerException, InputNumberNotInRangeException):
            return card_view(panier,means_of_payment_data)
    
    return choice

    
def wallet_view(panier, wallet_ok):
    clear_console()
    color_print("[WALLET]", BLUE)
    print("You choose wallet for purchase")

    if not wallet_ok:
        color_print("You don't have enough in your account",RED) 
        input("\nPress enter to continue...")

    
def shop_panier_bought_sucess_view(total_price):
    clear_console()

    print("Total : " + str(total_price) + "€")

    print("Ongoing treatment ... wait ...") 
    time.sleep(3)

    color_print("Congratulations ! You have purchased the products in your cast", GREEN)
    input("\nPress enter to continue...")