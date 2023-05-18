from app.model.objet import Objet
from app.model.objet_instance import ObjetInstance
from app.view.shop_panier import shop_panier_view,shop_panier_delete_elem_view
from app.controller.shop_panier_bought import shop_panier_bought
from app.model.panier import Panier
from app.model.utilisateur import Utilisateur
from app.model.jeu import Jeu

def shop_panier(username):
     utilisateur = Utilisateur.select_userid(username)
     panier_id = utilisateur.user_id
    
     #Récupère les ids des jeux dans le panier
     game_in_panier = Panier.get_jeux(Panier(panier_id))
     objet_in_panier = Panier.get_objet_instances(Panier(panier_id))
     game_ids = []
     objet_ids = []
     data_game_in_panier = []
     data_objet_in_panier = []

     for id in game_in_panier:
          game_ids.append(id.game_id)

     for id in objet_in_panier:
          objet_ids.append(id.id)

     #Récupère les données des jeux
     for game_id in game_ids:
          jeu = Jeu.select(game_id)
          data_game_in_panier.append((jeu.game_id,jeu.nom, jeu.prix))

     for objet_id in objet_ids:
          objetI = ObjetInstance.select(objet_id)
          realObjet = Objet.select(objetI.objet)
          data_objet_in_panier.append((realObjet.nom, realObjet.description, realObjet.price))


     data_user_choice = shop_panier_view(username,data_game_in_panier, data_objet_in_panier)
     user_choice,total_price = data_user_choice
     match user_choice:
          case 1:
               shop_panier_bought(username,data_game_in_panier,total_price) 
          case 2:
               user_choice_del_elem = shop_panier_delete_elem_view(data_game_in_panier)
               if user_choice == 0:
                    shop_panier(username)
               else:
                    Panier.remove_jeu(Panier(panier_id), Jeu(user_choice_del_elem))
                    shop_panier(username)
          case 3:
               return
         