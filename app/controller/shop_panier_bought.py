import datetime
from pickle import FALSE
from app.view.shop_panier_bought import  shop_panier_bought_view,wallet_view,card_view,shop_panier_bought_sucess_view
from app.model.moyen_paiement import MoyenPaiement
from app.model.utilisateur import Utilisateur
from app.model.panier import Panier
from app.model.achat import Achat
from app.model.jeu import Jeu

def shop_panier_bought(username,panier,total_price):
    

    user_choice = shop_panier_bought_view(panier)
    means_of_payment = user_choice

    match means_of_payment:
        case 1:
            shop_panier_bought_card(username,panier,total_price)
        case 2:
            shop_panier_bought_wallet(username,panier,total_price)
        case 3:
            return

def shop_panier_bought_card(username,panier,total_price):
    means_of_payment_data = MoyenPaiement.select_all()
    
    choice = card_view(panier,means_of_payment_data)
    if (choice == 0):
        return
    else:
        means_of_payment_choice = MoyenPaiement.select(int(choice))
        

        #Ajoute la taxe au prix à payer 
        total_price += means_of_payment_choice.taxe_du_moyen
        utilisateur = Utilisateur.select_userid(username)
        data_user = Utilisateur.select(utilisateur.user_id)
        panier_id = utilisateur.user_id
        Panier.update(Panier(total_price,panier_id))

        #Sauvegarde l'achat
        achat = Achat(montant_total=total_price, date_achat=datetime.date.today(), utilisateur=utilisateur.user_id, moyen_paiement=means_of_payment_choice.moyen_paiement_id, panier=panier_id)
        Achat.insert(achat)

        #Sauvegarde les produits sur le compte de l'user
        for game_id, _, _ in panier:
            Utilisateur.add_jeu(Utilisateur(utilisateur.user_id), Jeu(game_id), 0)

        #Vide le panier
        for game_id, _, _ in panier:
            Panier.remove_jeu(Panier(panier_id), Jeu(game_id))

        
        shop_panier_bought_sucess_view(total_price)


def shop_panier_bought_wallet(username,panier,total_price):   
    utilisateur = Utilisateur.select_userid(username)
    data_user = Utilisateur.select(utilisateur.user_id)
    panier_id = utilisateur.user_id
    argent_dispo = data_user.wallet
    wallet_ok = argent_dispo >= total_price 

    wallet_view(panier,wallet_ok)
    if wallet_ok:

        #Update wallet
        data_user.wallet = argent_dispo - total_price
        Utilisateur.update_wallet(Utilisateur(data_user.wallet,data_user.user_id))

        #Sauvegarde l'achat
        achat = Achat(montant_total=total_price, date_achat=datetime.date.today(), utilisateur=utilisateur.user_id, moyen_paiement=0, panier=panier_id)
        Achat.insert(achat)

        #Sauvegarde les produits sur le compte de l'user
        for game_id, _, _ in panier:
            Utilisateur.add_jeu(Utilisateur(utilisateur.user_id), Jeu(game_id), 0)

        #Vide le panier
        for game_id, _, _ in panier:
            Panier.remove_jeu(Panier(panier_id), Jeu(game_id))

        shop_panier_bought_sucess_view()
    else:
        shop_panier_bought(username,panier,total_price)
   


    