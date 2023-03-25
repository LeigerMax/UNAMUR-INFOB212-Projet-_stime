import mysql.connector
import os

##################################
###   GESTION BASE DE DONNEES  ###
##################################

connection = mysql.connector.connect(
    user='root', password='root', host='localhost', port="3306", database='dbstime')
print("DB connected")

cursor = connection.cursor()
cursor.execute('Select * FROM user')
users = cursor.fetchall()
connection.close()


##################################
###          TERMINAL          ###
##################################

# Nettoyer le terminal
def clear_terminal():
    if os.name == "posix":
        os.system("clear")
    else:
        os.system("cls")


# Quitter le terminal
def leave():
    clear_terminal()
    print("Leave the Stime platform...")
    exit()


##################################
###          LIBRARY           ###
##################################


def show_library():
    clear_terminal()
    print('\033[1;34m[YOUR LIBRARY]\033[0m \n')

    ## produire le SQL query en dessous
    # Récupérer les jeux de l'utilisateur dans la base de données
    games = [('Game Title 1',), ('Game Title 2',), ('Game Title EXTRA LONG 3',), ('Game Title 4',)]  # A SUPPRIMER

    if len(games) == 0:
        print("You don't have any games yet. You can visit the shop for buy a new game")
    else:
        # print("You have" + numberGames + " games \n")

        # Longueur maximale des titres de jeu
        game_title_size = 0
        for game in games:
            if len(game[0]) > game_title_size:
                game_title_size = len(game[0])

        # Espace devant le titre
        space_before_title = 2

        # Largeur totale du tableau
        total_width = (space_before_title * 2) + game_title_size

        # Ligne supérieure du tableau
        print('|' + '-' * (total_width + 2) + '|')

        # Afficher les titres de jeu dans des cellules de tableau
        for game in games:
            game_title = game[0]
            padding_width = total_width - len(game_title) - (space_before_title * 2)
            padding = ' ' * padding_width
            print(f'|{" " * space_before_title}{game_title}{padding}{" " * space_before_title}  |')
            # Ligne inférieur du tableau
            print('|' + '-' * (total_width + 2) + '|')


##################################
###         GAME SHOP          ###
##################################

def show_game_shop():
    clear_terminal()
    print('\033[1;34m[STORE]\033[0m \n')

    ## produire le SQL query en dessous


##################################
###         ITEM SHOP          ###
##################################

def show_item_shop():
    clear_terminal()
    print('\033[1;34m[ITEM MARKET]\033[0m \n')

    ## produire le SQL query en dessous


##################################
###         INVENTORY          ###
##################################

def my_item():
    clear_terminal()
    print('\033[1;34m[YOUR ITEM]\033[0m \n')

    ## produire le SQL query en dessous


##################################
###      MENU PLATFORME        ###
##################################

def show_menu():
    clear_terminal()
    username = "max"

    print("Welcome \033[1;34m" + username + "\033[0m ! \n")
    print('what do you wish to do ? Enter the number you wish for :')
    print('1.  See my games')
    print('2.  Buy a game')
    print('3.  Buy / sell an item')
    print('4.  See my items')
    print('5.  Leave')
    print('')

    choice2 = int(input())

    match choice2:
        case 1:
            show_library()
        case 2:
            show_game_shop()
        case 3:
            show_item_shop()
        case 4:
            my_item()
        case 5:
            leave()


##################################
###       LOGIN/REGISTRE       ###
##################################


## fonction d'inscription
def register():
    clear_terminal()
    print('\033[1;34m[REGISTER]\033[0m \n')
    print('Please enter the following information:')
    print('Choose a username')
    username = str(input())
    print('What is your password')
    password = str(input())
    print('What is your firstname')
    firstname = str(input())
    print('What is your name')
    name = str(input())
    print('What is your email')
    email = str(input())

    ## retravailler, pose soucis
    ##
    ##
    # sql = "INSERT INTO user (Username, Password, Firstname, Surname, Email, Birthdate, DateInscription) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    # now = date.today()
    # val = (username, password, firstname, name, email, now, now)
    # cursor.execute(sql, val)
    # Une fois l'inscription effecuté
    login_register_menu()


## fonction login
def login():
    clear_terminal()
    print('\033[1;34m[LOGIN]\033[0m \n')
    print('Please enter the following information:')
    print('Enter your username')
    username = str(input())
    print('Enter your password')
    password = str(input())
    show_menu()

    ## produire le SQL query en dessous
    ##IF login OK -> show_menu()


## fonction menu login/register
def login_register_menu():
    clear_terminal()
    print("\033[1;34m********************************************")
    print("*                                          *")
    print("*       Welcome to the Stime platform!     *")
    print("*                                          *")
    print("******************************************** \033[0m \n")
    print('What do you wish to do ? Enter the number you wish for :')
    print('1.  Register')
    print('2.  Login')
    print('3.  Leave')

    choice1 = int(input())

    match choice1:
        case 1:
            register()
        case 2:
            login()
        case 3:
            leave()


login_register_menu()
