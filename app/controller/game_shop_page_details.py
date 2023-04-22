from app.model.game import Game
from app.model.language import Language

from app.view.game_shop import game_shop_view
from mysql.connector import *
from app.settings import Database
from app.view.menu import main_menu_view
from app.view.game_shop_page_details import game_shop_page_details_view


def game_shop_page_details(username,gameId):

    game_list = Game().select_game_shop_details_page(gameId)
    #languages = Language.select_language_of_game(gameNumber)
    languages = Language.select_language_all_games()

    game_shop_page_details_view(game_list,languages)

    input()
