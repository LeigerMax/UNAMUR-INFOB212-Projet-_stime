from app.view.console_utils.colors import BLUE,GREEN
from app.view.console_utils.io import color_print, clear_console
from app.model.language import Language
from app.exceptions import UserInputNotAnIntegerException, InputNumberNotInRangeException
from app.view.console_utils.io import int_input


def game_shop_page_details_view(gameNumber,languages,avisList):
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
        color_print("Available in GamePass !", GREEN)

    if(gameNumber[5] == True):
        print("This is a DLC of <DLC GAME>, so you must own the original game in order to purchase this product.")

    #TODO: créer les avis
    print("\nReview game")

    
def game_shop_page_details_in_library_view():
    print("You already have the product in your library")

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
