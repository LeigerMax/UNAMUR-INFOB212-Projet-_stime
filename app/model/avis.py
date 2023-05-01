from app.database.connector import with_connection, get_cursor


class Avis:
    def __init__(self, avis_id=None, game_id=None, auteur=None, date=None, note=None, commentaire=None):
        self.avis_id = avis_id
        self.game_id = game_id
        self.auteur = auteur
        self.date = date
        self.note = note
        self.commentaire = commentaire

    @classmethod
    @with_connection
    def select(cls, avis_id, **kwargs):

        # get cursor from connection in kwargs
        cursor = get_cursor(kwargs)

        # execute query
        query = "SELECT * FROM AVIS WHERE AvisId = %s"
        cursor.execute(query, (avis_id))

        return Avis(*cursor.fetchone())

    @classmethod
    @with_connection
    def select_all(cls, **kwargs):

        # get cursor from connection in kwargs
        cursor = get_cursor(kwargs)

        # execute query
        query = "SELECT * FROM AVIS"
        cursor.execute(query)

        # instantiate all avis from cursor
        avis = []
        for avisI in cursor.fetchall():
            avis.append(Avis(*avisI))

        return avis
    
    @classmethod
    @with_connection
    def insert(cls, avis, **kwargs):

        # get cursor from connection in kwargs
        cursor = get_cursor(kwargs)

        # execute query
        query = "INSERT INTO AVIS (Jeu, Auteur, Date, Note, Commentaire) VALUES (%s, %s, %s, %s, %s, %s)"
        cursor.execute(query, (avis.jeu, avis.auteur, avis.date, avis.note, avis.commentaire))

        # store new id
        avis.avis_id = cursor.lastrowid

        return avis
    
    @classmethod
    @with_connection
    def update(cls, avis, **kwargs):

        # get cursor from connection in kwargs
        cursor = get_cursor(kwargs)

        # execute query
        query = "UPDATE AVIS SET Jeu = %s, Auteur = %s, Date = %s, Note = %s, Commentaire = %s WHERE AvisId = %s"
        cursor.execute(query, (avis.game_id, avis.auteur, avis.date, avis.note, avis.commentaire, avis.avis_id))

        return avis
    
    @classmethod
    @with_connection
    def delete(cls, avis, **kwargs):

        # get cursor from connection in kwargs
        cursor = get_cursor(kwargs)

        # execute query
        query = "DELETE FROM AVIS WHERE AchatId = %s"
        cursor.execute(query, (avis))

        return cursor.rowcount > 0
