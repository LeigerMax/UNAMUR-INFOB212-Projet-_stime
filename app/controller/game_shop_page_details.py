from app.model.jeu import Jeu
from app.model.langue import Langue
from app.model.jeu_langue_texte import JeuLangueTexte
from app.model.jeu_langue_audio import JeuLangueAudio
from app.model.image import Image
from app.model.utilisateur import Utilisateur
from app.model.panier import Panier
from app.controller.shop_panier import shop_panier

from app.view.game_shop_page_details import game_shop_page_details_view,game_shop_page_details_in_library_view,game_shop_page_details_buy_sub_view,game_shop_page_details_buy_view,take_game_free_sucess_view


def game_shop_page_details(username,gameId):

    game_list = Jeu.select(gameId)
    languages_text = JeuLangueTexte.select_langue_with_gameID(gameId) 
    languages_audio = JeuLangueAudio.select_langue_with_gameID(gameId) 
    images_game = Image.select_with_gameID(gameId) 



    #TODO: Récuperer les avis du jeu.
    #TODO: Check si jeu déjà acheter.
    utilisateurId = Utilisateur.select_userid(username)
    acheterCheck = False

    games_user = Utilisateur.get_games(utilisateurId)
    for game in games_user:
        if game.game_id == gameId:
            acheterCheck = True
            break
        else:
            acheterCheck = False

    #TODO: Check si abonnement GamePass.
    abonnementCheck = True

    information_game = [game_list, languages_text, languages_audio, images_game]

    game_shop_page_details_view(information_game,avisList=None) #TODO: Modifier None

    if(acheterCheck):
        game_shop_page_details_in_library_view()
        input();
    elif(not acheterCheck and abonnementCheck):
        user_choice = game_shop_page_details_buy_sub_view()
        match user_choice:
            case 1:
                #TODO: ADD library 
                take_game_free_sucess_view()
                input()
                return
            case 2:
                panier_id = utilisateurId.user_id
                Panier.add_jeu(Panier(panier_id), Jeu(gameId))
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

    


