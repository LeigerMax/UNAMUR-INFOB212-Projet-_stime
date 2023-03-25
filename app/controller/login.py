from app.view.login import login_menu


def login():
    credentials_ok = False
    first_try = True

    while not credentials_ok:
        if first_try:
            credentials = login_menu()
        else:
            credentials = login_menu("Credentials incorrect")

        # TODO: check credentials

        credentials_ok = True

