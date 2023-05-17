from app.exceptions import InputNotAnEmailException, InputNumberNotInRangeException, InputStringNotInRangeException, UserInputNotAnIntegerException
from app.view.console_utils.colors import BLUE
from app.view.console_utils.io import color_print, clear_console, date_input, email_input, int_input, password_input, string_input


def profil_view(username,data_user,data_user_bill_adress,data_user_delivery_adress):
    clear_console()
    color_print("[PROFIL]", BLUE)

    # Afficher les données de l'user
    for key, value in data_user.__dict__.items():
         if key not in ["password", "user_id", "panier","bill_address","delivery_address"]:
            print(key + ": " + str(value))
            
    # Afficher les données de l'adresse de facturation
    print("\nBill Address:")
    if data_user_bill_adress is not None:
        for key, value in data_user_bill_adress.__dict__.items():
            print(key + ": " + str(value))

    # Afficher les données de l'adresse de livraison
    print("\nDelivery Address:")
    if data_user_delivery_adress is not None:
        for key, value in data_user_delivery_adress.__dict__.items():
            print(key + ": " + str(value))
            

    #Choix du profil
    options = """
    Choose option
    1.  Edit
    2.  Delete Account
    3.  Leave
        """
    
    print(options)
    try:
        choice_profil = int_input(1, 3, placeholder="Choice: ")
    except (UserInputNotAnIntegerException, InputNumberNotInRangeException):
        return profil_view(username,data_user,data_user_bill_adress,data_user_delivery_adress)
    
    return choice_profil

def profil_edit_view(username,data_user,data_user_bill_adress,data_user_delivery_adress):
    clear_console()
    color_print("[EDIT PROFIL]", BLUE)

    options = """
        Please choice information for edit
        1.  Firstname {}
        2.  Lastname {}
        3.  Email {}
        4.  Password 
        5.  Bill Adress 
        6.  Delivery Adress 
        7.  Leave
            """.format(
        data_user.firstname,
        data_user.lastname,
        data_user.email,
    )
    
        
    print(options)
    try:
        choice_profil = int_input(1, 7, placeholder="Choice: ")
    except (UserInputNotAnIntegerException, InputNumberNotInRangeException):
        return profil_view(username,data_user)
    
    return choice_profil



def profil_edit_firstname_view(username):
    clear_console()
    color_print("[EDIT PROFIL]", BLUE)

    try:
        firstname = string_input(placeholder="Your firstname: ")
    except InputStringNotInRangeException:
        return profil_edit_firstname_view("One or many fields do not respect size limit")

    return firstname


def profil_edit_lastname_view(username):
    clear_console()
    color_print("[EDIT PROFIL]", BLUE)
    
    try:
       lastname = string_input(placeholder="Your lastname: ")
    except InputStringNotInRangeException:
        return profil_edit_lastname_view("One or many fields do not respect size limit")

    return lastname
    


def profil_edit_email_view(username):
    clear_console()
    color_print("[EDIT PROFIL]", BLUE)

    try:
        email = email_input(placeholder="Your email address: ")
    except InputNotAnEmailException:
        return profil_edit_email_view("Email is not valid")
    
    return email



def profil_edit_password_view(username):
    clear_console()
    color_print("[EDIT PROFIL]", BLUE)

    try:
        password = password_input(placeholder="Your password: ")
        password_confirm = password_input(placeholder="Confirm password: ")
    except InputNotAnEmailException:
        return profil_edit_password_view("Email is not valid")
    
    return password
    


def profil_edit_bill_adress_view(username):
    clear_console()
    color_print("[EDIT PROFIL]", BLUE)

    try:
        new_numero = string_input(placeholder="Please enter the house number: ")
        new_rue = string_input(placeholder="Please enter the street name: ")
        new_ville = string_input(placeholder="Please enter the city: ")
        new_code_postal = string_input(placeholder="Please enter the postal code: ")
        new_pays = string_input(placeholder="Please enter the country: ")

    except InputStringNotInRangeException:
        return profil_edit_bill_adress_view(username)
    bill_address = [new_numero, new_rue, new_ville, new_code_postal, new_pays]

    # Retourner l'adresse de facturation sous forme de liste
    return bill_address



def profil_edit_delivery_adress_view(username):
    clear_console()
    color_print("[EDIT PROFIL]", BLUE)

    try:
        new_numero = string_input(placeholder="Please enter the house number: ")
        new_rue = string_input(placeholder="Please enter the street name: ")
        new_ville = string_input(placeholder="Please enter the city: ")
        new_code_postal = string_input(placeholder="Please enter the postal code: ")
        new_pays = string_input(placeholder="Please enter the country: ")

    except InputStringNotInRangeException:
        return profil_edit_bill_adress_view(username)
    delivery_address = [new_numero, new_rue, new_ville, new_code_postal, new_pays]
    
    # Retourner l'adresse de livraison sous forme de liste
    return delivery_address



def profil_delete_view(username,data_user):
    clear_console()
    color_print("[DELETE PROFIL]", BLUE)
    print("Your profile has been deleted")
    