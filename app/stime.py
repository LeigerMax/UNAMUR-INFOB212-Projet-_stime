import os
from app.view.console_utils.io import clear_console

##################################
###          LIBRARY           ###
##################################

def show_library():
    clear_console()
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
    clear_console()
    print('\033[1;34m[STORE]\033[0m \n')

    ## produire le SQL query en dessous


##################################
###         ITEM SHOP          ###
##################################

def show_item_shop():
    clear_console()
    print('\033[1;34m[ITEM MARKET]\033[0m \n')

    ## produire le SQL query en dessous


##################################
###         INVENTORY          ###
##################################

def my_item():
    clear_console()
    print('\033[1;34m[YOUR ITEM]\033[0m \n')

    ## produire le SQL query en dessous









login_register_menu()
