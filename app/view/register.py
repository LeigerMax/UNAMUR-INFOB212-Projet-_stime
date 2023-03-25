from app.exceptions import InputStringNotInRangeException, InputNotAnEmailException
from app.view.console_utils.colors import BLUE, RED_BLD
from app.view.console_utils.io import clear_console, color_print, string_input, password_input, email_input


def register_view(error_message=None):
    """
    Show register form, then return user inputs.
    :param error_message: a message to display
    :return: the option selected
    """

    clear_console()
    color_print("[REGISTER]", BLUE)
    if error_message:
        color_print(error_message, RED_BLD)

    print("Please enter the following information:")

    try:
        username = string_input(placeholder="New username: ")
        password = password_input(placeholder="Your password: ")
        password_confirm = password_input(placeholder="Confirm password: ")
        firstname = string_input(placeholder="Your firstname: ")
        lastname = string_input(placeholder="Your lastname: ")
        email = email_input(placeholder="Your email address: ")
    except InputStringNotInRangeException:
        return register_view("One or many fields do not respect size limit")
    except InputNotAnEmailException:
        return register_view("Email is not valid")

    return {
        "username": username,
        "password": password,
        "confirm_password": password_confirm,
        "firstname": firstname,
        "lastname": lastname,
        "email": email
    }


    ## retravailler, pose soucis
    ##
    ##
    # sql = "INSERT INTO user (Username, Password, Firstname, Surname, Email, Birthdate, DateInscription) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    # now = date.today()
    # val = (username, password, firstname, name, email, now, now)
    # cursor.execute(sql, val)
    # Une fois l'inscription effecuté

    #login_register_menu()