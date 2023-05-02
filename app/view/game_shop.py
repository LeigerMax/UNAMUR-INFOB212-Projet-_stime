from app.view.console_utils.colors import BLUE
from app.view.console_utils.io import color_print, clear_console, int_input
from app.exceptions import UserInputNotAnIntegerException, InputNumberNotInRangeException


def game_shop_view(games):
    clear_console()
    color_print("[STORE]", BLUE)


    # Fonction pour tronquer une chaîne de caractères à une longueur donnée
    def tronquer_chaine(chaine, longueur_max):
        if len(chaine) <= longueur_max:
            return chaine
        else:
            return chaine[:longueur_max-3] + "..."

    # Déterminer la largeur maximale de la colonne "Jeu" & le nombre de jeu
    jeu_total = 0
    largeur_max_jeu = 0

    for jeu in games:
        if(len(jeu.nom) > largeur_max_jeu):
            largeur_max_jeu = len(jeu.nom)
        jeu_total = jeu_total+1

    # Afficher les données dans la table formatée avec un numéro devant chaque jeu
    print("| {:<4} | {:<{}} | {:<80} | {:<7} |".format("Num", "Title", largeur_max_jeu, "Description", "Price"))
    print("+{}+{}+{}+{}+".format("-"*6, "-"*(largeur_max_jeu+2), "-"*82, "-"*9))
    for i, jeu in enumerate(games, start=1):
        jeu_tronque = tronquer_chaine(jeu.nom, largeur_max_jeu)
        description_tronquee = tronquer_chaine(jeu.description, 80)
        print("| {:<4} | {:<{}} | {:<80} | {:<6.2f}€ |".format(i, jeu_tronque, largeur_max_jeu, description_tronquee, jeu.prix))


    options = """
    What do you want to do ?
    Game number you want to explore
    0. for leave
    """
    print(options)

    try:
        return int_input(0, jeu_total, placeholder="Choice: ") #TODO jeu_total not working 
    except (UserInputNotAnIntegerException, InputNumberNotInRangeException):
        return game_shop_view(games)
