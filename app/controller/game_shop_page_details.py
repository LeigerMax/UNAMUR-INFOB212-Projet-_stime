import datetime
from app.model.evaluation import Evaluation
from app.model.jeu import Jeu
from app.model.langue import Langue
from app.model.jeu_langue_texte import JeuLangueTexte
from app.model.jeu_langue_audio import JeuLangueAudio
from app.model.image import Image
from app.model.avis import Avis
from app.model.utilisateur import Utilisateur
from app.model.panier import Panier
from app.controller.shop_panier import shop_panier

from app.view.game_shop_page_details import eval_review_game, eval_take_review_game, game_shop_page_details_view,game_shop_page_details_in_library_view,game_shop_page_details_buy_sub_view,game_shop_page_details_buy_view,take_game_free_sucess_view, writing_review_game


def game_shop_page_details(username,gameId):

    game_list = Jeu.select(gameId)
    languages_text = JeuLangueTexte.select_langue_with_gameID(gameId) 
    languages_audio = JeuLangueAudio.select_langue_with_gameID(gameId) 
    images_game = Image.select_with_gameID(gameId) 


    utilisateurId = Utilisateur.select_userid(username)

    avisList = Avis.select_with_gameID(gameId)


    # Check si jeu déjà acheter.
    acheter_check = False

    games_user = Utilisateur.get_games(utilisateurId)
    for game in games_user:
        if game.game_id == gameId:
            acheter_check = True
            break
        else:
            acheter_check = False

    # Si DLC
    if(game_list.dlc is not None ):
        dlc_game_name = Jeu.select(game_list.dlc) 
    else:
        dlc_game_name = None



    abonnementCheck = abonnementCheck = Utilisateur.get_current_abonnement(utilisateurId)

    information_game = [game_list, languages_text, languages_audio, images_game, dlc_game_name]

    game_shop_page_details_view(information_game,avisList)

    # Si jeu acheter
    if(acheter_check):
        #TODO: UPDATE AVIS
        user_choice = game_shop_page_details_in_library_view()

        match user_choice:
            case 1:
                user_choice_interne = eval_review_game(avisList)
                if user_choice_interne == 0:
                    game_shop_page_details(username,gameId)
                else:
                    data_review_select = Avis.select(user_choice_interne)
                    data_eval_review = Evaluation.select_with_avisID(user_choice_interne)
                    choice_approuve = eval_take_review_game(data_review_select,data_eval_review)
                    match choice_approuve:
                        case 1:
                            Evaluation.insert(Evaluation(utilisateurId.user_id,user_choice_interne, 1,None ))
                            game_shop_page_details(username,gameId)
                        case 2:
                            Evaluation.insert(Evaluation(utilisateurId.user_id,user_choice_interne, 0,None ))
                            game_shop_page_details(username,gameId)
                        case 3:
                            game_shop_page_details(username,gameId)

            case 2:
                data_writing_review =  writing_review_game()
                writing_review(gameId,utilisateurId,data_writing_review)
                game_shop_page_details(username,gameId)

            case 3:
                return
        
    
    # Si jeu pas acheter
    elif(not acheter_check and abonnementCheck):
        user_choice = game_shop_page_details_buy_sub_view()

        match user_choice:
            case 1:
                Utilisateur.add_jeu(Utilisateur(utilisateurId.user_id), Jeu(gameId), True)
                take_game_free_sucess_view()
                input()
                return
            
            case 2:
                panier_id = utilisateurId.user_id
                Panier.add_jeu(Panier(panier_id), Jeu(gameId))
                shop_panier(username)

            case 3:
                user_choice_interne = eval_review_game(avisList)
                if user_choice_interne == 0:
                    game_shop_page_details(username,gameId)
                else:
                    data_review_select = Avis.select(user_choice_interne)
                    data_eval_review = Evaluation.select_with_avisID(user_choice_interne)
                    choice_approuve = eval_take_review_game(data_review_select,data_eval_review)
                    match choice_approuve:
                        case 1:
                            Evaluation.insert(Evaluation(utilisateurId.user_id,user_choice_interne, 1,None ))
                            game_shop_page_details(username,gameId)
                        case 2:
                            Evaluation.insert(Evaluation(utilisateurId.user_id,user_choice_interne, 0,None ))
                            game_shop_page_details(username,gameId)
                        case 3:
                            game_shop_page_details(username,gameId)

            case 4:
                return


    elif(not acheter_check):
        user_choice = game_shop_page_details_buy_view()

        match user_choice:
            case 1:
                panier_id = utilisateurId.user_id
                Panier.add_jeu(Panier(panier_id), Jeu(gameId))
                shop_panier(username)

            case 2:
                user_choice_interne = eval_review_game()
                if user_choice_interne == 0:
                    game_shop_page_details(username,gameId)
                else:
                    data_review_select = Avis.select(user_choice_interne)
                    data_eval_review = Evaluation.select_with_avisID(user_choice_interne)
                    choice_approuve = eval_take_review_game(data_review_select,data_eval_review)
                    match choice_approuve:
                        case 1:
                            Evaluation.insert(Evaluation(utilisateurId.user_id,user_choice_interne, 1,None ))
                            game_shop_page_details(username,gameId)
                        case 2:
                            Evaluation.insert(Evaluation(utilisateurId.user_id,user_choice_interne, 0,None ))
                            game_shop_page_details(username,gameId)
                        case 3:
                            game_shop_page_details(username,gameId)
            case 3:
                return



def writing_review(gameId,utilisateurId,data_writing_review):

    # Création et écupération des informations depuis la view 
    note = data_writing_review["note"]
    commentaire = data_writing_review["commentaire"]
    game_id = gameId
    auteur = utilisateurId.user_id
    date = datetime.date.today()

    # Check si insert ou update et sauvegarde dans la BDD
    existing_avis = Avis.select_auteur_gameId(auteur,game_id)
    if existing_avis:
        print("Update not possible, assume !")
        input()
        #Avis.update(Avis(existing_avis.avis_id,game_id, auteur, date, note, commentaire ))
    else:
        Avis.insert(Avis(None,game_id, auteur, date, note, commentaire ))
    
    return


    

