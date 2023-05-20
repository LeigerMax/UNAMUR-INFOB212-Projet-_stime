from app.view.console_utils.colors import BLUE,GREEN, RED
from app.view.console_utils.io import color_print, clear_console, string_input
from app.model.langue import Langue
from app.exceptions import InputStringNotInRangeException, UserInputNotAnIntegerException, InputNumberNotInRangeException
from app.view.console_utils.io import int_input
from app.view.login_register import register_view


def game_shop_page_details_view(information_game,avisList):

    gameNumber = information_game[0]
    languages_text = information_game[1]
    languages_audio = information_game[2]
    images_game = information_game[3]
    game_name_dlc = information_game[4]
    categories = information_game[5]
    developer = information_game[6]
    publisher = information_game[7]


    clear_console()
    color_print(f"[DETAILS PAGE OF {gameNumber.nom} ]", BLUE)

    # Affichage des détails du jeu
    print(f"Game Title: {gameNumber.nom}") 

    print("Categories:")
    for category in categories:
        print(f"- {category.nom}")

    print(f"Developer: {developer.nom}")
    print(f"Publisher: {publisher.nom}")
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


    # Affichage des avis
    print("\nReview game\n")
    if avisList is None or len(avisList) == 0:
        print("No reviews available for this game.")
    else:
        print("Reviews:")
        for i, avis in enumerate(avisList, 1):
            print(f"{i}. User: {avis.username}")
            print(f"   Rating: {avis.note}/10")
            print(f"   Comment: {avis.commentaire}")
            print(f"   Date: {avis.date}/10")
            print()

    
def game_shop_page_details_in_library_view():
    print("You already have the product in your library")
    print("Do you want to evaluate a review or write a review ? ")
    options = """
    1. Evaluate a review
    2. Write a review
    3. No (leave)
    """
    print(options)
    try:
        return int_input(1, 3, placeholder="Choice: ") 
    except (UserInputNotAnIntegerException, InputNumberNotInRangeException):
        return game_shop_page_details_in_library_view()
    

def game_shop_page_details_buy_sub_view():
    print("Do you want purchase or take this product (Free your during your subscription)  / evaluate a review / write a review ? ")
    options = """
    1. Yes, take free
    2. Yes, purchase this product
    3. Evaluate a review
    4. No (leave)
    """
    print(options)
    try:
        return int_input(1, 4, placeholder="Choice: ") 
    except (UserInputNotAnIntegerException, InputNumberNotInRangeException):
        return game_shop_page_details_view()

def game_shop_page_details_buy_view():
    print("Do you want purchase this product / evaluate a review / write a review ?")
    options = """
    1. Yes, purchase this product
    2. Evaluate a review
    3. No (leave)
    """
    print(options)

    try:
        return int_input(1, 3, placeholder="Choice: ") 
    except (UserInputNotAnIntegerException, InputNumberNotInRangeException):
        return game_shop_page_details_view()



def take_game_free_sucess_view():
    print("Congratulations ! You take this product")
    print("\nPress enter to leave...")


def writing_review_game():
    print("Write a Review")
    print("--------------------")
    try:
        note = int_input(placeholder="Rating: ")
        commentaire = string_input(placeholder="Comment: ")
    except InputStringNotInRangeException:
        return register_view("One or many fields do not respect size limit")

    return {
        "note": note,
        "commentaire": commentaire
    }


def eval_review_game(avisList):
    clear_console()
    color_print(f"[REVIEW GAME]", BLUE)
    if avisList is None or len(avisList) == 0:
        print("No reviews available for this game.")
    else:
        print("Reviews:")
        for i, avis in enumerate(avisList, 1):
            print(f"{i}. User: {avis.username}")
            print(f"   Rating: {avis.note}/10")
            print(f"   Comment: {avis.commentaire}")
            print(f"   Date: {avis.date}")
            print()


    options = """
        What do you want to do ?
        Number review want opened
        0. for leave
        """

    print(options)

    try:
        choice = int_input(0, len(avisList), placeholder="Choice: ")
    except (UserInputNotAnIntegerException, InputNumberNotInRangeException):
            return eval_review_game(avisList)
    
    if choice == 0:
        return 0
    else:
        selected_review = avisList[choice - 1]
        return selected_review.avis_id


def eval_take_review_game(data_review_select,data_eval_review):
    clear_console()

    print("Review:")
    print(f"User: {data_review_select.username}")
    print(f"Rating: {data_review_select.note}/10")
    print(f"Comment: {data_review_select.commentaire}")
    print(f"Date: {data_review_select.date}")

    print("\nEvaluation:")

    for evaluation in data_eval_review:
        print(f"User: {evaluation.username}")
        if evaluation.approuve == 0:
            color_print(f"Not Approuve", RED)
        else:
            color_print(f"Approuve", BLUE)
            
        print()

    options = """
        Do you approve of the review or not?
        1. Approved the review
        2. Disapproved the review
        0. For leave
        """

    print(options)

    try:
        return int_input(0, 2, placeholder="Choice: ")
    except (UserInputNotAnIntegerException, InputNumberNotInRangeException):
            return eval_take_review_game(data_review_select,data_eval_review)



