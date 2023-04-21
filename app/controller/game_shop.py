from app.model.store import Store

from app.view.game_shop import game_shop_view
from mysql.connector import *
from app.settings import Database


def game_shop():

    game_list = Store().select_all_games_shop_page()

    game_shop_view(game_list)
    input()
