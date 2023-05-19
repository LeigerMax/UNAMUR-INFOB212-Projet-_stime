

from app.view.console_utils.colors import BLUE
from app.view.console_utils.io import clear_console, color_print


def entreprise_profil_details_view(data_entreprise):
    clear_console()
    color_print("[ENTREPRISE DETAILS]", BLUE)


    # Afficher le nom et la description de l'entreprise
    for entreprise in data_entreprise:
        print(f"Name: {entreprise.nom}") 
        print(f"Description: {entreprise.description}") 
        print(f"Website: {entreprise.adresse_web}") 
        break


    print("----------------------------------------------------")
    print("\Games produced by the company:")

    for entreprise in data_entreprise:
        print(f"- {entreprise.nom_jeu}") 

    print("\nPress enter to leave...")