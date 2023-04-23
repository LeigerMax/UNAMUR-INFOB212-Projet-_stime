from app.view.shop_panier import shop_panier_view

def shop_panier(username):
     panier = [("Jeu 1", 19.99), ("Jeu 2", 29.99), ("Jeu 3", 9.99), ("Jeu 4", 14.99)]
     #TODO: panier in DB
     shop_panier_view(panier)
     input()