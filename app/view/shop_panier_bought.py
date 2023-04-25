from app.view.console_utils.colors import BLUE,GREEN,RED
from app.view.console_utils.io import color_print, clear_console, int_input,string_input
from app.exceptions import UserInputNotAnIntegerException, InputNumberNotInRangeException,InputStringNotInRangeException
import time

def shop_panier_bought_view(panier):
    clear_console()
    color_print("[BOUGHT]", BLUE)

    #Demande si c'est à livrer
    options = """
    Do you want the product to be delivered ?
    Note : Only games and dlcs can be delivered !
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


def card_view(panier,means_of_payment_data):
    clear_console()
    color_print("[CARD]", BLUE)
    print("You choose card for purchase")
    
    print("What means of payment?")
    for i in range(len(means_of_payment_data)):
        means_of_payment = means_of_payment_data[i]
        print(i,". ", means_of_payment[0], " avec ", means_of_payment[1], "€ de taxe")

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


def shop_panier_bought_delivery_view(panier,adress):
    clear_console()
    color_print("[DELIVERY]", BLUE)

    # Si l'adresse est nulle, demander à l'utilisateur d'entrer une nouvelle adresse
    if not adress:
        try:
            new_numero = string_input(placeholder="Please enter the house number: ")
            new_rue = string_input(placeholder="Please enter the street name: ")
            new_ville = string_input(placeholder="Please enter the city: ")
            new_code_postal = string_input(placeholder="Please enter the postal code: ")
            new_pays = string_input(placeholder="Please enter the country: ")
        except InputStringNotInRangeException:
            return shop_panier_bought_delivery_view(panier,adress)
        delivery_address = [new_numero, new_rue, new_ville, new_code_postal, new_pays]

    # Sinon, donner à l'utilisateur le choix entre garder la même adresse ou entrer une nouvelle adresse        
    else:
        print("Current delivery address: ")
        for i in range(len(adress)):
            address_data = adress[i]
            print("Number :", address_data[0])
            print("Street :", address_data[1])
            print("City :", address_data[2])
            print("Postal :", address_data[3])
            print("Country :", address_data[4])

        options = """
        Do you want to keep the same address?
        1.  Yes
        2.  No
        """
        print(options)

        try:
            choice = int_input(1, 2, placeholder="Choice: ")
            if choice == 1:
                delivery_address = adress
            elif choice == 2:
                try:
                    new_numero = string_input(placeholder="Please enter the house number: ")
                    new_rue = string_input(placeholder="Please enter the street name: ")
                    new_ville = string_input(placeholder="Please enter the city: ")
                    new_code_postal = string_input(placeholder="Please enter the postal code: ")
                    new_pays = string_input(placeholder="Please enter the country: ")
                except InputStringNotInRangeException:
                    return shop_panier_bought_delivery_view(panier,adress)
                delivery_address = [new_numero, new_rue, new_ville, new_code_postal, new_pays]
        except (UserInputNotAnIntegerException, InputNumberNotInRangeException):
            return shop_panier_bought_delivery_view(panier,adress)

    # Retourner l'adresse de livraison sous forme de liste
    return delivery_address

    
def shop_panier_bought_sucess_view():
    clear_console()

    print("Ongoing treatment ... wait ...") 
    time.sleep(3)

    color_print("Congratulations ! You have purchased the products in your cast", GREEN)
    input("\nPress enter to continue...")