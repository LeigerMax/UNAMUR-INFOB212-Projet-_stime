from app.model.game import Game

from app.view.game_shop import game_shop_view
from app.view.menu import main_menu_view
from app.controller.game_shop_page_details import game_shop_page_details


def game_shop(username):

    game_list = Game.select_all()

    user_choice = game_shop_view(game_list)

    if user_choice == 0:
        main_menu_view(username)
    else:
        game_shop_page_details(username,user_choice)


    #input()
