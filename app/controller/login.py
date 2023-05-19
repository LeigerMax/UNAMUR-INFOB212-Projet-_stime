from app.database.connector import update_user_password
from app.model.jeu import Jeu
from app.view.login_register import login_view
from app.view.menu import main_menu_view
from app.model.utilisateur import Utilisateur


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

            # update DB username and password
            update_user_password(credentials["username"], credentials["password_clear"])

            # check if abonnement has expired and delete GamePass games if so
            delete = False
            utilisateur_id = Utilisateur.select_userid(username)
            abonnement_check = Utilisateur.get_current_abonnement(utilisateur_id)

            if abonnement_check is not None and abonnement_check.type == "Basique":
                games_user = Utilisateur.get_games(utilisateur_id)
                for game in games_user:
                    if (Utilisateur.check_take_gamepass(utilisateur_id, Jeu(game.game_id)) is not None) and (abonnement_check.type == "Basique"):
                        Utilisateur.remove_jeu(utilisateur_id, Jeu(game.game_id))
                        delete = True

                if delete:
                    print("You have a basique subscription, your games taken with GamePass have been deleted from your account")
                    input()

            main_menu_view(username)
        else:
            first_try = False
            credentials = login_view()

    return username
