from app.exceptions import UserInputNotAnIntegerException, InputNumberNotInRangeException, \
    InputStringNotInRangeException, InputNotAnEmailException
from app.view.console_utils.colors import BLUE, RED_BLD
from app.view.console_utils.io import clear_console, color_print, int_input, string_input, password_input, email_input


##################################
###          LIBRARY           ###
##################################

def library_view(games):
    """
    Display games of the user in a beautiful array.
    :param games: the list of games to show
    """

    # games = [('Game Title 1',), ('Game Title 2',), ('Game Title EXTRA LONG 3',), ('Game Title 4',)]  # A SUPPRIMER

    clear_console()
    color_print("[YOUR LIBRARY]", BLUE)

    if len(games) == 0:
        print("You don't have any games yet. You can visit the shop to buy new games.")
    else:
        print(f"You have {len(games)} game(s).\n")

        # Max length for game titles
        game_title_size = 0
        for game in games:
            if len(game[0]) > game_title_size:
                game_title_size = len(game[0])

        # Spaces before title
        space_before_title = 2

        # Total width
        total_width = (space_before_title * 2) + game_title_size

        # Top of the array
        print('|' + '-' * (total_width + 2) + '|')

        for game in games:
            game_title = game[0]
            padding_width = total_width - len(game_title) - (space_before_title * 2)
            padding = ' ' * padding_width
            print(f'|{" " * space_before_title}{game_title}{padding}{" " * space_before_title}  |')
            # Lower lines for the array
            print('|' + '-' * (total_width + 2) + '|')


##################################
###         GAME SHOP          ###
##################################

def game_shop_view():
    # clear_console()
    # print('\033[1;34m[STORE]\033[0m \n')
    pass


##################################
###         ITEM SHOP          ###
##################################

def item_shop_view():
    # clear_console()
    # print('\033[1;34m[ITEM MARKET]\033[0m \n')
    pass


##################################
###         INVENTORY          ###
##################################

def my_item_view():
    # clear_console()
    # print('\033[1;34m[YOUR ITEM]\033[0m \n')
    pass


##################################
###      MENU PLATFORM         ###
##################################

def welcome_menu_view(error_message=None):
    """
    Show login and register menu to console, then return user choice.
    :param error_message: a message to display
    :return: the option selected
    """

    header = """
********************************************
*                                          *
*       Welcome to the Stime platform!     *
*                                          *
********************************************
    """

    options = """
What do you want to do ?
1.  Register
2.  Login
3.  Leave
    """

    clear_console()
    color_print(header, BLUE)
    print(options)
    if error_message:
        color_print(error_message, RED_BLD)

    try:
        return int_input(1, 3, placeholder="Choice: ")
    except (UserInputNotAnIntegerException, InputNumberNotInRangeException):
        return welcome_menu_view("Invalid input")


def main_menu_view(username, error_message=None):
    """
    Show main menu when connected, then return user choice.
    :param username: name of the connected user.
    :param error_message: a message to display
    :return: the option selected
    """

    welcome_msg = f"Welcome {username} !"

    options = """
What do you want to do ?
1.  See my games
2.  Buy a game
3.  Buy / sell an item
4.  See my items
5.  Leave
    """

    clear_console()
    color_print(welcome_msg, BLUE)
    print(options)
    if error_message:
        color_print(error_message, RED_BLD)

    try:
        return int_input(1, 5, placeholder="Choice: ")
    except (UserInputNotAnIntegerException, InputNumberNotInRangeException):
        return main_menu_view(username, "Invalid input")


##################################
###       LOGIN/REGISTER       ###
##################################

def login_menu_view(error_message=None):
    """ Show login menu, then return user inputs. """

    clear_console()
    color_print("[LOGIN]", BLUE)
    if error_message:
        color_print(error_message, RED_BLD)

    try:
        username = string_input(placeholder="Username: ")
        password = password_input(placeholder="Password: ")
    except InputStringNotInRangeException:
        return login_menu_view("Username or password does not respect size limit")

    return {
        "username": username,
        "password": password
    }


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