import datetime
from app.view.console_utils.colors import BLUE
from app.view.console_utils.io import color_print, clear_console, int_input
from app.exceptions import UserInputNotAnIntegerException, InputNumberNotInRangeException

def shop_panier_view(username,jeu, objets,soldeList):
    clear_console()
    color_print("[CAST]", BLUE)

    total_price = 0

    #afficher la liste de jeu dans le panier
    if len(jeu) == 0 and len(objets) == 0:
        print("The cart is empty.")
        print("Cart empty, please add items and come back here")
        input()
        return 3,total_price
    else:
        print("Product in the cart:")
        for i, jeu in enumerate(jeu):
            game_id,nom_jeu, prix_jeu,solde = jeu
            if solde is not None :
                for j, soldeSelect in enumerate(soldeList):
                    if(solde == soldeSelect.solde_id) and (datetime.date.today() >= soldeSelect.date_debut_solde) and (datetime.date.today() <= soldeSelect.date_fin_solde):
                        taux_solde = soldeSelect.taux_solde 
                        total_price += prix_jeu * ( 100 - taux_solde ) / 100
                        print(f"{i + 1}. Game name: {nom_jeu} | Price (SALES): {prix_jeu:.2f} €")
                        break
            else : 
                total_price += prix_jeu
                print(f"{i + 1}. Game name: {nom_jeu} | Price: {prix_jeu:.2f} €")

            
        for j, objets in enumerate(objets):
            id_objet, nom_objet, descr_objet, prix_objet = objets
            total_price += prix_objet
            print(f"{j + 1 + len(jeu)}. Item name: {nom_objet} | Price: {prix_objet:.2f} €")

        print(f"Total: {total_price:.2f} €")

        #Option
        options = """
        What do you want to do ?
        1.  Buy cart
        2.  Delete a element
        3.  Leave
            """

        print(options)
        try:
            return int_input(1, 3, placeholder="Choice: "),total_price
        except (UserInputNotAnIntegerException, InputNumberNotInRangeException):
            return shop_panier_view(username,jeu, objets,soldeList)



def shop_panier_delete_elem_view(panier,objets):
    clear_console()
    color_print("[DELETE ELEM PANIER]", BLUE)
    
    if len(panier) == 0 and len(objets) == 0:
        print("The cart is empty.")
    else:
        print("Games or items in the cart:")
        for i, jeu in enumerate(panier):
            game_id, nom_jeu, prix_jeu = jeu
            print(f"{i + 1}. Game name: {nom_jeu} | Price: {prix_jeu:.2f} €")
        for j, objets in enumerate(objets):
            nom_objet, descr_objet, prix_objet = objets
            print(f"{j + 1 + len(panier)}. Item name: {nom_objet} | Price: {prix_objet} €")

        print("Enter the number of the game or item you want to remove (0 to cancel): ")
        try:
            choice = int_input(0, len(panier), placeholder="Choice: ")
            if(choice == 0):
                return None #Return sans rien delete
            else:
                return panier[choice - 1][0]  # Return the game_id
        except (UserInputNotAnIntegerException, InputNumberNotInRangeException):
            return shop_panier_delete_elem_view(panier)

        

