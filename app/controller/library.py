from app.model.game import Game

from app.view.library import library_view


def library(username):

    
    game_list = Game().select_all()

    library_view(game_list)

    input()
