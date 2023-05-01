from app.view.login_register import login_view
from app.view.menu import main_menu_view
from app.model.user import User
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
        
        check_user = User.check_user_login(username, password)
        if check_user is not None:
            credentials_ok = True
            main_menu_view(username)
        else:
            first_try = False
            credentials = login_view()   

    return username
