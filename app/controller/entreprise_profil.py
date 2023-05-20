
from app.controller.entreprise_profil_details import entreprise_profil_details
from app.model.entreprise import Entreprise
from app.view.entreprise_profil import entreprise_profil_view
from app.view.entreprise_profil_details import entreprise_profil_details_view
from app.view.menu import main_menu_view

def entreprise_profil(username):


    entreprise_list = Entreprise.select_all()
    user_choice = entreprise_profil_view(entreprise_list)

    if user_choice == 0:
        main_menu_view(username)
    else:
        entreprise_profil_details(username,user_choice)
