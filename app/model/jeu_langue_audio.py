from app.database.connector import with_connection, get_cursor


class JeuLangueAudio:
    def __init__(self, langue=None, game_id=None):
        self.langue = langue
        self.game_id = game_id

    @classmethod
    @with_connection
    def select_langue_with_gameID(cls, gameId, **kwargs):
        # get cursor from connection in kwargs
        cursor = get_cursor(kwargs)

        # execute query
        query = "SELECT l.Langue, l.Raccourci FROM JEU_LANGUE_AUDIO jla INNER JOIN LANGUE l ON jla.Langue = l.Langue WHERE jla.Jeu = %s "
        cursor.execute(query, (gameId,))

        # instantiate all langues from cursor
        langues = []
        for langue in cursor.fetchall():
            langues.append(JeuLangueAudio(*langue))

        return langues