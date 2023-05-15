from app.database.connector import with_connection, get_cursor
from app.model.categorie import Categorie
from app.model.langue import Langue


class Jeu:
    def __init__(self, game_id=None, nom=None, description=None, date_de_sortie=None, prix=None, game_pass=None, developpeur=None, editeur=None, solde=None, est_dlc=None, dlc=None):
        self.game_id = game_id
        self.nom = nom
        self.description = description
        self.date_de_sortie = date_de_sortie
        self.prix = prix
        self.game_pass = game_pass
        self.developpeur = developpeur
        self.editeur = editeur
        self.solde = solde
        self.est_DLC = est_dlc
        self.dlc = dlc
    
    @classmethod
    @with_connection
    def select(cls, gameId, **kwargs):
        # get cursor from connection in kwargs
        cursor = get_cursor(kwargs)

        # execute query
        query = "SELECT * FROM JEU WHERE GameId = %s"
        cursor.execute(query, (gameId,))

        try:
            return Jeu(*cursor.fetchone())
        except TypeError:
            return None
    
    @classmethod
    @with_connection
    def select_all(cls, **kwargs):
        # get cursor from connection in kwargs
        cursor = get_cursor(kwargs)

        # execute query
        query = "SELECT * FROM JEU"
        cursor.execute(query)

        # instantiate all games from cursor
        games = []
        for game in cursor.fetchall():
            games.append(Jeu(*game))

        return games

    @classmethod
    @with_connection
    def insert(cls, game, **kwargs):
        # get cursor from connection in kwargs
        cursor = get_cursor(kwargs)

        # execute query
        query = "INSERT INTO GAME (Nom, Description, DateDeSortie, Prix, GamePass, Developpeur, Editeur, Solde, EstDLC, DLC) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        cursor.execute(query, (game.nom, game.description, game.date_de_sortie, game.prix, game.game_pass, game.developpeur, game.editeur, game.solde, game.est_DLC, game.dlc))

        # store new id
        game.game_id = cursor.lastrowid

        return game

    @classmethod
    @with_connection
    def update(cls, game, **kwargs):
        # get cursor from connection in kwargs
        cursor = get_cursor(kwargs)

        # execute query
        query = "UPDATE GAME SET Nom = %s, Description = %s, DateDeSortie = %s, Prix = %s, GamePass = %s, Developpeur = %s, Editeur = %s, Solde = %s, EstDLC = %s, DLC = %s WHERE GameId = %s"
        cursor.execute(query, (game.name, game.description, game.date_de_sortie, game.prix, game.game_pass, game.developpeur, game.editeur, game.solde, game.est_DLC, game.dlc, game.game_id))

        return game

    @classmethod
    @with_connection
    def delete(cls, game_id, **kwargs):
        # get cursor from connection in kwargs
        cursor = get_cursor(kwargs)

        # execute query
        query = "DELETE FROM GAME WHERE GameId = %s"
        cursor.execute(query, (game_id))

        return cursor.rowcount > 0

    #############################
    #  Jeu-Categorie functions  #
    #############################

    @classmethod
    @with_connection
    def get_categories(cls, jeu, **kwargs):
        """
        Get all categories of a game
        :param jeu: the jeu
        :return: the categories of the game
        """

        # get cursor from connection in kwargs
        cursor = get_cursor(kwargs)

        # execute query
        query = "SELECT c.* FROM CATEGORIE as c, CATEGORIE_JEU as cj WHERE c.Nom = cj.Categorie AND cj.Jeu = %s"
        cursor.execute(query, (jeu.game_id))

        # instantiate all categories from cursor
        categories = []
        for categorie in cursor.fetchall():
            categories.append(Categorie(*categorie))

        return categories

    ##########################
    #  Jeu-Langue functions  #
    ##########################

    @classmethod
    @with_connection
    def get_langue_text(cls, jeu, **kwargs):
        """
        Get all langues for the text of a game
        :param jeu: the jeu
        :return: all langues of the game used in text
        """

        # get cursor from connection in kwargs
        cursor = get_cursor(kwargs)

        # execute query
        query = "SELECT l.* FROM LANGUE as l, JEU_LANGUE_TEXTE as jlt WHERE l.Langue = jlt.Langue AND jlt.Jeu = %s"
        cursor.execute(query, (jeu.game_id))

        # instantiate all langues from cursor
        langues = []
        for langue in cursor.fetchall():
            langues.append(Langue(*langue))

        return langues

    @classmethod
    @with_connection
    def get_langue_audio(cls, jeu, **kwargs):
        """
        Get all langues for the audio of a game
        :param jeu: the jeu
        :return: all langues of the game used in audio
        """

        # get cursor from connection in kwargs
        cursor = get_cursor(kwargs)

        # execute query
        query = "SELECT l.* FROM LANGUE as l, JEU_LANGUE_AUDIO as jla WHERE l.Langue = jla.Langue AND jla.Jeu = %s"
        cursor.execute(query, (jeu.game_id))

        # instantiate all langues from cursor
        langues = []
        for langue in cursor.fetchall():
            langues.append(Langue(*langue))

        return langues