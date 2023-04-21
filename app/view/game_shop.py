from app.view.console_utils.colors import BLUE
from app.view.console_utils.io import color_print, clear_console


def game_shop_view(games):
    clear_console()
    color_print("[STORE]", BLUE)


    # Fonction pour tronquer une chaîne de caractères à une longueur donnée
    def tronquer_chaine(chaine, longueur_max):
        if len(chaine) <= longueur_max:
            return chaine
        else:
            return chaine[:longueur_max-3] + "..."

    # Déterminer la largeur maximale de la colonne "Jeu"
    largeur_max_jeu = max(len(jeu[0]) for jeu in games)

    # Afficher les données dans la table formatée avec un numéro devant chaque jeu
    print("| {:<4} | {:<{}} | {:<100} | {:<7} |".format("Num", "Jeu", largeur_max_jeu, "Description", "Prix"))
    print("+{}+{}+{}+{}+".format("-"*6, "-"*(largeur_max_jeu+2), "-"*102, "-"*9))
    for i, jeu in enumerate(games, start=1):
        jeu_tronque = tronquer_chaine(jeu[0], largeur_max_jeu)
        description_tronquee = tronquer_chaine(jeu[1], 100)
        print("| {:<4} | {:<{}} | {:<100} | {:<6.2f}€ |".format(i, jeu_tronque, largeur_max_jeu, description_tronquee, jeu[2]))





    print("\nPress enter to continue...")
