from app.view import login_menu_view


def login():
    credentials_ok = False
    first_try = True
    username = None

    while not credentials_ok:
        if first_try:
            credentials = login_menu_view()
        else:
            credentials = login_menu_view("Credentials incorrect")

        # TODO: check credentials
        username = credentials["username"]

        credentials_ok = True

    return username
