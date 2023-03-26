from app.view import register_view


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
