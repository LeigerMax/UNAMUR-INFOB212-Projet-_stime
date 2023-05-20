from app.exceptions import InputNumberNotInRangeException, UserInputNotAnIntegerException
from app.view.console_utils.colors import BLUE
from app.view.console_utils.io import color_print, clear_console, int_input

def entreprise_profil_view(entreprise_list):
    clear_console()
    color_print("[ENTREPRISE LIST]", BLUE)


    # Fonction pour tronquer une chaîne de caractères à une longueur donnée
    def tronquer_chaine(chaine, longueur_max):
        if len(chaine) <= longueur_max:
            return chaine
        else:
            return chaine[:longueur_max-3] + "..."

    # Déterminer la largeur maximale de la colonne "Nom" & le nombre d'entreprise
    entreprise_total = 0
    largeur_max_nom = 0

    for entrep in entreprise_list:
        if(len(entrep.nom) > largeur_max_nom):
            largeur_max_nom = len(entrep.nom)
        entreprise_total = entreprise_total+1

    # Afficher les données dans la table formatée avec un numéro devant chaque jeu
    print("| {:<4} | {:<{}} | {:<80} |".format("Num", "Nom", largeur_max_nom, "Description"))
    print("+{}+{}+{}+".format("-"*6, "-"*(largeur_max_nom+2), "-"*82))
    for i, entrep in enumerate(entreprise_list, start=1):
        entrep_tronque = tronquer_chaine(entrep.nom, largeur_max_nom)
        description_tronquee = tronquer_chaine(entrep.description, 80)
        print("| {:<4} | {:<{}} | {:<80} |".format(i, entrep_tronque, largeur_max_nom, description_tronquee))

    options = """
    What do you want to do ?
    Entreprise number you want to explore
    0. for leave
    """
    print(options)

    try:
        choice = int_input(0, len(entreprise_list), placeholder="Choice: ") 
    except (UserInputNotAnIntegerException, InputNumberNotInRangeException):
        return entreprise_profil_view(entreprise_list)
    
    selected_review = entreprise_list[choice-1]
    return selected_review.nom