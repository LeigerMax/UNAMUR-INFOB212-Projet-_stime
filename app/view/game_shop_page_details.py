from app.view.console_utils.colors import BLUE
from app.view.console_utils.io import color_print, clear_console
from app.model.language import Language
from app.exceptions import UserInputNotAnIntegerException, InputNumberNotInRangeException
from app.view.console_utils.io import int_input


def game_shop_page_details_view(gameNumber,languages):
    clear_console()
    color_print(f"[DETAILS PAGE OF {gameNumber[1]} ]", BLUE)

    # Affichage des détails du jeu
    print(f"Game Title: {gameNumber[1]}") 
    print("Genre: <Genre du jeu>")
    print("Developer: <Développeur du jeu>")
    print("Publisher: <Éditeur du jeu>")
    print(f"Release Date: {gameNumber[3]}")
    print(f"Price: {gameNumber[4]} €")
    print(f"Description: {gameNumber[2]}")
    print("Game picture: <Image du jeu")

    
    print("Languages support :")
    for language in languages:
        print(f" - {language[0]} ( {language[1]} ) ")

    if(gameNumber[6] == True):
        print("Available in GamePass !")

    if(gameNumber[5] == True):
        print("This is a DLC of <DLC GAME>, so you must own the original game in order to purchase this product.")

    #IF DEJA ACHETER 
        # print("You already have the product in your library")
    #IF ELSE PAS ACHETER
        # ACHAT --> redirige vers une page achat qui va choisir le moyen de paiement, soustraire l'argent sur le compte et ajouter le jeu dans la table achat de l'user
    #ELSE 
        # Return game_shop 

    #try:
    #    return int_input(1, 3, placeholder="Choice: ")
    #except (UserInputNotAnIntegerException, InputNumberNotInRangeException):
    #    return game_shop_page_details_view("Invalid input")

    print("\nPress enter to continue...")


