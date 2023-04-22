from app.model.game import Game
from app.model.language import Language

from app.view.game_shop_page_details import game_shop_page_details_view,game_shop_page_details_review_view


def game_shop_page_details(username,gameId):

    game_list = Game().select_game_shop_details_page(gameId)
    #languages = Language.select_language_of_game(gameNumber) #TODO: A remettre plus tard
    languages = Language.select_language_all_games()

    #TODO: Récuperer les avis du jeu.

    game_shop_page_details_view(game_list,languages)
    game_shop_page_details_review_view(avisList=None) #TODO: Modifier None

    #TODO: Récuperer le choix de l'user. Soit leave, soit acheter le jeu
    #TODO: Check Si il y a déjà le jeu dans sa libraire
    #TODO: Ajouter le jeu si pas dans la libraire et possède GamePass
    #TODO: Ajouter un avis si jeu acheter

    input()


