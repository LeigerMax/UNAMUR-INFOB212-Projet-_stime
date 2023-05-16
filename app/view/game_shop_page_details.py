from app.view.console_utils.colors import BLUE,GREEN
from app.view.console_utils.io import color_print, clear_console
from app.model.langue import Langue
from app.exceptions import UserInputNotAnIntegerException, InputNumberNotInRangeException
from app.view.console_utils.io import int_input


def game_shop_page_details_view(information_game,avisList):

    gameNumber = information_game[0]
    languages_text = information_game[1]
    languages_audio = information_game[2]
    images_game = information_game[3]
    game_name_dlc = information_game[4]


    clear_console()
    color_print(f"[DETAILS PAGE OF {gameNumber.nom} ]", BLUE)

    # Affichage des détails du jeu
    print(f"Game Title: {gameNumber.nom}") 
    print("Genre: <Genre du jeu>")
    print("Developer: <Développeur du jeu>")
    print("Publisher: <Éditeur du jeu>")
    print(f"Release Date: {gameNumber.date_de_sortie}")
    print(f"Price: {gameNumber.prix} €")
    print(f"Description: {gameNumber.description}")
    for image in images_game:
        print(f"Game picture: {image.alt}")

    
    print("Languages support text :")
    for language in languages_text:
        print(f" - {language.langue}  ") #TOTO: Mettre les raccourcis ( {language.raccourci} )

    print("Languages support audio :")
    for language in languages_audio:
        print(f" - {language.langue}  ") #TOTO: Mettre les raccourcis ( {language.raccourci })

    if(gameNumber.game_pass == True):
        color_print("Available in GamePass !", GREEN)

    if(gameNumber.est_DLC == True):
        print(f"This is a DLC of {game_name_dlc.nom}, so you must own the original game in order to purchase this product.")

    #TODO: créer les avis
    print("\nReview game")

    
def game_shop_page_details_in_library_view():
    print("You already have the product in your library")
    print("Press enter to continue")

def game_shop_page_details_buy_sub_view():
    print("Do you want purchase or take this product ? (Free your during your subscription)")
    options = """
    1. Yes, take free
    2. Yes, purchase this product
    3. No (leave)
    """
    print(options)
    try:
        return int_input(1, 3, placeholder="Choice: ") 
    except (UserInputNotAnIntegerException, InputNumberNotInRangeException):
        return game_shop_page_details_view()

def game_shop_page_details_buy_view():
    print("Do you want purchase this product ?")
    options = """
    1. Yes, purchase this product
    2. No (leave)
    """
    print(options)

    try:
        return int_input(1, 2, placeholder="Choice: ") 
    except (UserInputNotAnIntegerException, InputNumberNotInRangeException):
        return game_shop_page_details_view()


def take_game_free_sucess_view():
    print("Congratulations ! You take this product")
    print("\nPress enter to leave...")
