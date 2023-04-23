from app.model.game import Game
from app.model.language import Language
from app.controller.game_shop import game_shop
from app.controller.shop_panier import shop_panier

from app.view.game_shop_page_details import game_shop_page_details_view,game_shop_page_details_in_library_view,game_shop_page_details_buy_sub_view,game_shop_page_details_buy_view


def game_shop_page_details(username,gameId):

    game_list = Game().select_game_shop_details_page(gameId)
    #languages = Language.select_language_of_game(gameNumber) #TODO: A remettre plus tard
    languages = Language.select_language_all_games()

    #TODO: Récuperer les avis du jeu.
    #TODO: Check si jeu déjà acheter.
    acheterCheck = False
    #TODO: Check si abonnement GamePass.
    abonnementCheck = True

    game_shop_page_details_view(game_list,languages,avisList=None) #TODO: Modifier None

    if(acheterCheck):
        game_shop_page_details_in_library_view()
    elif(not acheterCheck and abonnementCheck):
        user_choice = game_shop_page_details_buy_sub_view()
        match user_choice:
            case 1:
                #TODO: ADD library 
                print("ok")
            case 2:
                shop_panier(username)
            case 3:
                game_shop(username)

    elif(not acheterCheck):
        user_choice = game_shop_page_details_buy_view()
        match user_choice:
            case 1:
                shop_panier(username)
            case 2:
                game_shop(username)


    #TODO: Récuperer le choix de l'user. Soit leave, soit acheter le jeu
    #TODO: Check Si il y a déjà le jeu dans sa libraire
    #TODO: Ajouter le jeu si pas dans la libraire et possède GamePass
    #TODO: Ajouter un avis si jeu acheter

    input()


