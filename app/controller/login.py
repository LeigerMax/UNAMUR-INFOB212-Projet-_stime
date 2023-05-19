from app.model.jeu import Jeu
from app.view.login_register import login_view
from app.view.menu import main_menu_view
from app.model.utilisateur import Utilisateur
from app.view.console_utils.io import color_print
from app.view.console_utils.colors import RED_BLD


def login():
    credentials_ok = False
    first_try = True
    username = None

    while not credentials_ok:
        if first_try:
            credentials = login_view()

        username = credentials["username"]
        password = credentials["password"]
        
        check_user = Utilisateur.check_user_login(username, password)
        if check_user is not None:
            credentials_ok = True
            delete = False
            utilisateurId = Utilisateur.select_userid(username)
            abonnementCheck = Utilisateur.get_current_abonnement(utilisateurId)
            if(abonnementCheck.type == "Basique"):
                games_user = Utilisateur.get_games(utilisateurId)
                for game in games_user:
                    if (Utilisateur.check_take_gamepass(utilisateurId,Jeu(game.game_id)) is not None) and (abonnementCheck.type == "Basique"):
                            Utilisateur.remove_jeu(utilisateurId,Jeu(game.game_id))
                            delete = True

                if(delete):
                    print("You have a basique subscription, your games taken with GamePass have been deleted from your account")
                    input()            

            main_menu_view(username)
        else:
            first_try = False
            credentials = login_view()   

    return username
