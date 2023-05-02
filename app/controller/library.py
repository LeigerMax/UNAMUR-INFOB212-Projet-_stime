from app.model.jeu import Jeu

from app.view.library import library_view


def library(username):

    
    game_list = Jeu.select_all()

    library_view(game_list)

    input()
