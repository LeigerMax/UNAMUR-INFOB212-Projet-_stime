from app.model.jeu import Jeu
from app.model.utilisateur import Utilisateur

from app.view.library import library_view


def library(username):

    #Récupère la liste des jeux de l'user
    utilisateurId = Utilisateur.select_userid(username)
    game_list = Utilisateur.get_games(utilisateurId)

    library_view(game_list)

    input()
