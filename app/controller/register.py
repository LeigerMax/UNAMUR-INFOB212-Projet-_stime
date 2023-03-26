from app.view.login_register import register_view


def register():
    fields_ok = False
    first_try = True
    username = None

    while not fields_ok:
        if first_try:
            user_information = register_view()
        else:
            user_information = register_view("One or more fields are not correct")

        # TODO: check if fields are valid
        username = user_information["username"]
        fields_ok = True

    return username

    # sql = "INSERT INTO user (Username, Password, Firstname, Surname, Email, Birthdate, DateInscription) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    # now = date.today()
    # val = (username, password, firstname, name, email, now, now)
    # cursor.execute(sql, val)
    # Une fois l'inscription effecuté