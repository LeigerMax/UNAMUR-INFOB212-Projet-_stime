from app.view.console_utils.colors import BLUE
from app.view.console_utils.io import clear_console, color_print


def library_view(games):
    """
    Display games of the user in a beautiful array.
    :param games: the list of games to show
    """

    clear_console()
    color_print("[YOUR LIBRARY]", BLUE)

    if len(games) == 0:
        print("You don't have any games yet. You can visit the shop to buy new games.")
    else:
        print(f"You have {len(games)} game(s).\n")

        
        # Fonction pour tronquer une chaîne de caractères à une longueur donnée
        def tronquer_chaine(chaine, longueur_max):
            if len(chaine) <= longueur_max:
                return chaine
            else:
                return chaine[:longueur_max-3] + "..."

        # Déterminer la largeur maximale de la colonne "Jeu"
        largeur_max_jeu = max(len(jeu.nom) for jeu in games)

        # Afficher les données dans la table formatée avec un numéro devant chaque jeu
        print("| {:<4} | {:<{}} | {:<100} |".format("Num", "Jeu", largeur_max_jeu, "Description"))
        print("+{}+{}+{}+".format("-"*6, "-"*(largeur_max_jeu+2), "-"*102))
        for i, jeu in enumerate(games, start=1):
            jeu_tronque = tronquer_chaine(jeu.nom, largeur_max_jeu)
            description_tronquee = tronquer_chaine(jeu.description, 100)
            print("| {:<4} | {:<{}} | {:<100} |".format(i, jeu_tronque, largeur_max_jeu, description_tronquee))



    print("\nPress enter to continue...")
