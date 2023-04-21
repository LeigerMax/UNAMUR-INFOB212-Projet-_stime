from app.model.store import Store

from app.view.library import library_view


def library(username):

    
    game_list = Store().select_all_games_shop_page()

    library_view(game_list)

    input()
