from app.database.connector import update_user_password
from app.model.jeu import Jeu
from app.view.login_register import login_view
from app.view.menu import utilisateur_menu_view
from app.model.utilisateur import Utilisateur
from database.roles import Roles


def login():
    credentials_ok = False
    first_try = True
    user = None

    while not credentials_ok:
        if first_try:
            credentials = login_view()

        username = credentials["username"]
        password = credentials["password"]

        user = Utilisateur.check_user_login(username, password)
        if user is not None:
            credentials_ok = True

            # update DB username and password
            update_user_password(username, credentials["password_clear"])

            # get complete user info from DB
            user = Utilisateur.select(user.user_id)

            # if abonnement has expired and delete GamePass games if so
            if user.role == Roles.UTILISATEUR_ROLE:
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
        else:
            first_try = False
            credentials = login_view()

    return user
