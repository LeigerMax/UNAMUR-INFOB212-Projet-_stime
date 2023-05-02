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
        
#        check_user = User.check_user_login(username, password)
#        if check_user is not None:
#            credentials_ok = True
#            main_menu_view(username)
#        else:
#            color_print("Error: Incorrect username or password. Please try again.", RED_BLD)
#            first_try = False
#            credentials = login_view()

       #TODO delete after
        credentials_ok = True    

    return username
