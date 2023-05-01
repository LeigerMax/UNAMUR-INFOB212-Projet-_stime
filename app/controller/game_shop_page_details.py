from app.model.game import Game
from app.model.langue import Langue
from app.controller.shop_panier import shop_panier

from app.view.game_shop_page_details import game_shop_page_details_view,game_shop_page_details_in_library_view,game_shop_page_details_buy_sub_view,game_shop_page_details_buy_view,take_game_free_sucess_view


def game_shop_page_details(username,gameId):

    game_list = Game().select(gameId)
    #languages = Language.select_language_of_game(gameNumber) #TODO: A remettre plus tard
    languages = Langue.select_language_all_games()

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
                take_game_free_sucess_view()
                input()
                return
            case 2:
                shop_panier(username)
            case 3:
                return

    elif(not acheterCheck):
        user_choice = game_shop_page_details_buy_view()
        match user_choice:
            case 1:
                shop_panier(username)
            case 2:
                return


    #TODO: Ajouter un avis si jeu acheter

    


