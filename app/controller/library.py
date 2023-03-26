from app.view.library import library_view


def library(username):

    # TODO: fetch user's games
    games = [('Game Title 1',), ('Game Title 2',), ('Game Title EXTRA LONG 3',), ('Game Title 4',)]

    library_view(games)

    input()
