from app.view.shop_panier_bought import shop_panier_bought_view,wallet_view,card_view

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
    #TODO: FAIRE ACHAT
    #TODO: VIDER le panier
    card_view(panier,is_livraison)
    input()

def shop_panier_bought_wallet(username,panier,is_livraison,total_price):    
    #TODO: SELECT wallet FROM USER
    #TODO: IF(is_livraison): SELECT taxeDuMoyen FROM MOYEN_PAEIMENT and panier_price(=total_price+taxeDuMoyen)
    #TODO: check si wallet >= panier_price 
    #      IF(True): card_view(panier,is_livraison)
    #      ELSE(): shop_panier_bought_wallet(username,panier,is_livraison) and print

    wallet_view(panier,is_livraison)

    input()

    