from app.view.shop_panier import shop_panier_view,shop_panier_delete_elem_view
from app.controller.shop_panier_bought import shop_panier_bought

def shop_panier(username):
     panier = [("Jeu 1", 19.99), ("Jeu 2", 29.99), ("Jeu 3", 9.99), ("Jeu 4", 14.99)]
     #TODO: panier in DB
     data_user_choice = shop_panier_view(username,panier)
     user_choice,total_price = data_user_choice
     match user_choice:
          case 1:
               shop_panier_bought(username,panier,total_price) 
          case 2:
               user_choice_del_elem = shop_panier_delete_elem_view(panier)
               if user_choice == 0:
                    shop_panier(username)
               else:
                    print("Del elem" +str(user_choice_del_elem))
                    #TODO: DELETE ELEM
                    #shop_panier(username)
          case 3:
               return
         
     #input()