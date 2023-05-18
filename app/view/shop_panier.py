from app.view.console_utils.colors import BLUE
from app.view.console_utils.io import color_print, clear_console, int_input
from app.exceptions import UserInputNotAnIntegerException, InputNumberNotInRangeException

def shop_panier_view(username,jeu, objets):
    clear_console()
    color_print("[CAST]", BLUE)

    total_price = 0

    #afficher la liste de jeu dans le panier
    if len(jeu) == 0 and len(objets) == 0:
        print("The cart is empty.")
    else:
        print("Games in the cart:")
        for i, jeu in enumerate(jeu):
            game_id,nom_jeu, prix_jeu = jeu
            total_price += prix_jeu
            print(f"{i + 1}. Game name: {nom_jeu} | Price: {prix_jeu} €")
        for j, objets in enumerate(objets):
            nom_objet, descr_objet, prix_objet = objets
            total_price += prix_objet
            print(f"{j + 1 + len(jeu)}. Item name: {nom_objet} | Price: {prix_objet} €")
        print(f"Total: {total_price} €")

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
        return shop_panier_view(jeu)


def shop_panier_delete_elem_view(panier,objets):
    clear_console()
    color_print("[DELETE ELEM PANIER]", BLUE)
    
    if len(panier) == 0 and len(objets) == 0:
        print("The cart is empty.")
    else:
        print("Games or items in the cart:")
        for i, jeu in enumerate(panier):
            game_id, nom_jeu, prix_jeu = jeu
            print(f"{i + 1}. Game name: {nom_jeu} | Price: {prix_jeu} €")
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

        

