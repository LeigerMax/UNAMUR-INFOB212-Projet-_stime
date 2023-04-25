from app.view.shop_panier_bought import shop_panier_bought_view,wallet_view,card_view,shop_panier_bought_delivery_view,shop_panier_bought_sucess_view

def shop_panier_bought(username,panier,total_price):

    user_choice = shop_panier_bought_view(panier)
    delivery, means_of_payment = user_choice

    if delivery == 1:
        print("The product will be delivered.")
        is_livraison = True
    else:
        print("The product will not be delivered.")
        is_livraison = False

    match means_of_payment:
        case 1:
            shop_panier_bought_card(username,panier,is_livraison,total_price)
        case 2:
            shop_panier_bought_wallet(username,panier,is_livraison,total_price)
        case 3:
            return

def shop_panier_bought_card(username,panier,is_livraison,total_price):
    #TODO: SELECT * USER Moyen_paiement
    means_of_payment_data = [("Paypal","5"), ("Bank","10")]
    if(is_livraison):
        #TODO: SELECT Adress USER and taxeDuMoyen
        adress = [("1","rue des disp","Namur","5000","Belgique")]
        taxe_delivery = 10
        #adress = ""
        delivery_data = shop_panier_bought_delivery_view(panier,adress)
        #TODO: SAVE delivery_data in DB
        choice = card_view(panier,means_of_payment_data)
        #TODO: Ajouter taxe dans total_price
        #      vider le panier
        #      Sauvegarder dans achat
        #      Sauvegarder les produits sur le compte
        shop_panier_bought_sucess_view()
    else:
        choice = card_view(panier,means_of_payment_data)
        #TODO: Ajouter taxe dans total_price
        #      vider le panier
        #      Sauvegarder dans achat
        #      Sauvegarder les produits sur le compte
        shop_panier_bought_sucess_view()


def shop_panier_bought_wallet(username,panier,is_livraison,total_price):   
    #TODO: SELECT portefeuille USER et ajoute dans argent_dispo
    argent_dispo = 50
    wallet_ok = argent_dispo >= total_price 
    if(is_livraison):
        #TODO: SELECT Adress USER et ajoute dans adress 
        adress = [("1","rue des disp","Namur","5000","Belgique")]
        #adress = ""
        delivery_data = shop_panier_bought_delivery_view(panier,adress)
        #TODO: SAVE delivery_data in DB
        wallet_view(panier,wallet_ok)
        if wallet_ok:
            #TODO: vider le panier
            #      Soustraire le portefeuille avec total_price (Select portefeuill, puis soustraire et update)
            #      Sauvegarder dans achat
            #      Sauvegarder les produits sur le compte
            shop_panier_bought_sucess_view()
        else:
            shop_panier_bought(username,panier,total_price)
    else:
        wallet_view(panier,wallet_ok)
        if wallet_ok:
            #TODO: vider le panier
            #      Soustraire le portefeuille avec total_price (Select portefeuill, puis soustraire et update)
            #      Sauvegarder dans achat
            #      Sauvegarder les produits sur le compte
            shop_panier_bought_sucess_view()
        else:
            shop_panier_bought(username,panier,total_price)
   


    