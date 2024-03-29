from app.model.jeu import Jeu

from app.view.game_shop import game_shop_view
from app.view.menu import utilisateur_menu_view
from app.controller.game_shop_page_details import game_shop_page_details


def game_shop(username):

    game_list = Jeu.select_all() 

    user_choice = game_shop_view(game_list)

    if user_choice == 0:
        utilisateur_menu_view(username)
    else:
        game_shop_page_details(username,user_choice)

