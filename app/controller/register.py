from app.view.login_register import register_view
from app.model.utilisateur import Utilisateur

import datetime

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
        #username = user_information["username"]
        #fields_ok = True

        # Récupération des informations d'utilisateur depuis la view
        username = user_information["username"]
        password = user_information["password"]
        confirm_password = user_information["confirm_password"]
        firstname = user_information["firstname"]
        lastname = user_information["lastname"]
        email = user_information["email"]
        date_of_birth = user_information["date_of_birth"]
        

        # Check si password et confirm_password sont identique
        try:
            if password != confirm_password:
                raise ValueError("Passwords do not match")

            fields_ok = True
        except ValueError as e:
            print(f"Error: {e}")

        first_try = False

    # Sauvegarde dans la BDD
    inscription_date = datetime.date.today()
    Utilisateur.insert_new_user(username, password, firstname, lastname, email, date_of_birth, inscription_date)

        
    return username