from app.view.login_register import login_view


def login():
    credentials_ok = False
    first_try = True
    username = None

    while not credentials_ok:
        if first_try:
            credentials = login_view()
        else:
            credentials = login_view("Credentials incorrect")

        # TODO: check credentials
        username = credentials["username"]
        credentials_ok = True

    return username
