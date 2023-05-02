from app.database.connector import with_connection, get_cursor


class JeuLangueTexte:
    def __init__(self, langue=None, game_id=None):
        self.langue = langue
        self.gameId = game_id

    @classmethod
    @with_connection
    def select_langue_with_gameID(cls, gameId, **kwargs):
        # get cursor from connection in kwargs
        cursor = get_cursor(kwargs)

        # execute query
        query = "SELECT l.Langue, l.Raccourci FROM JEU_LANGUE_TEXTE jlt INNER JOIN LANGUE l ON jlt.Langue = l.Langue WHERE jlt.Jeu = %s "
        cursor.execute(query, (gameId,))  

        # instantiate all langues from cursor
        langues = []
        for langue in cursor.fetchall():
            langues.append(JeuLangueTexte(*langue))

        return langues
