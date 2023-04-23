from app.view.console_utils.colors import BLUE
from app.view.console_utils.io import color_print, clear_console, int_input
from app.exceptions import UserInputNotAnIntegerException, InputNumberNotInRangeException

def shop_panier_view(panier):
    clear_console()
    color_print("[PANIER]", BLUE)

    total_price = 0

    #afficher la liste de jeu dans le panier
    if len(panier) == 0:
        print("The cart is empty.")
    else:
        print("Games in the cart:")
        for i, jeu in enumerate(panier):
            nom_jeu, prix_jeu = jeu
            total_price += prix_jeu
            print(f"{i + 1}. Game name: {nom_jeu} | Price: {prix_jeu} €")
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
        return int_input(1, 3, placeholder="Choice: ")
    except (UserInputNotAnIntegerException, InputNumberNotInRangeException):
        return shop_panier_view(panier)


def shop_panier_delete_elem_view(panier):
    clear_console()
    color_print("[DELETE ELEM PANIER]", BLUE)
    
    if len(panier) == 0:
        print("The cart is empty.")
    else:
        print("Games in the cart:")
        for i, jeu in enumerate(panier):
            nom_jeu, prix_jeu = jeu
            print(f"{i + 1}. Game name: {nom_jeu} | Price: {prix_jeu} €")

        print("Enter the number of the game you want to remove (0 to cancel): ")
        index = int_input()
        if index == 0:
            return
        elif index < 1 or index > len(panier):
            print("Invalid input.")
        else:
            nom_jeu, prix_jeu = panier[index - 1]
            panier.pop(index - 1)
            print(f"{nom_jeu} has been removed from the cart.")
