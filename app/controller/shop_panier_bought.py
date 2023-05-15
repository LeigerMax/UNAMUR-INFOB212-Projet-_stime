from app.view.shop_panier_bought import shop_panier_bought_view,wallet_view,card_view,shop_panier_bought_sucess_view
from app.model.moyen_paiement import MoyenPaiement
from app.model.utilisateur import Utilisateur
from app.model.panier import Panier

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
    means_of_payment_choice = MoyenPaiement.select(int(choice))
     

    #Ajoute la taxe au prix à payer 
    total_price += means_of_payment_choice.taxe_du_moyen
    utilisateur = Utilisateur.select_userid(username)
    panier_id = utilisateur.user_id
    Panier.update(Panier(total_price,panier_id))

    #Sauvegarde l'achat


    #Sauvegarde les produits sur le compte de l'user


    #Vide le panier



    
    shop_panier_bought_sucess_view(total_price)


def shop_panier_bought_wallet(username,panier,total_price):   
    #TODO: SELECT portefeuille USER et ajoute dans argent_dispo
    argent_dispo = 50
    wallet_ok = argent_dispo >= total_price 

    wallet_view(panier,wallet_ok)
    if wallet_ok:
        #TODO: vider le panier
        #      Soustraire le portefeuille avec total_price (Select portefeuill, puis soustraire et update)
        #      Sauvegarder dans achat
        #      Sauvegarder les produits sur le compte
        shop_panier_bought_sucess_view()
    else:
        shop_panier_bought(username,panier,total_price)
   


    