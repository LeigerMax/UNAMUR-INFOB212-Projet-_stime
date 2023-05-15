from app.database.connector import with_connection, get_cursor


class Objet:
    def __init__(self, objet_id=None, nom=None, description=None, game_id=None):
        self.objet_id = objet_id
        self.nom = nom
        self.description = description
        self.game_id = game_id
        
    @classmethod
    @with_connection
    def select(cls, objet_id, **kwargs):
        # get cursor from connection in kwargs
        cursor = get_cursor(kwargs)

        # execute query
        query = "SELECT * FROM OBJET WHERE ObjetId = %s"
        cursor.execute(query, (objet_id,))

        try:
            return Objet(*cursor.fetchone())
        except TypeError:
            return None

    @classmethod
    @with_connection
    def select_all(cls, **kwargs):
        # get cursor from connection in kwargs
        cursor = get_cursor(kwargs)

        # execute query
        query = "SELECT * FROM OBJET"
        cursor.execute(query)

        # instantiate all objet from cursor
        objets = []
        for objet in cursor.fetchall():
            objets.append(Objet(*objet))

        return objets
    
    @classmethod
    @with_connection
    def insert(cls, objet, **kwargs):
        # get cursor from connection in kwargs
        cursor = get_cursor(kwargs)

        # execute query
        query = "INSERT INTO OBJET (Nom, Description, Jeu) VALUES (%s, %s, %s)"
        cursor.execute(query, (objet.nom, objet.description, objet.jeu))

        # store new id
        objet.objet_id = cursor.lastrowid

        return objet

    @classmethod
    @with_connection
    def update(cls, objet, **kwargs):
        # get cursor from connection in kwargs
        cursor = get_cursor(kwargs)

        # execute query
        query = "UPDATE GAME SET Nom = %s, Description = %s, Jeu = %s WHERE ObjetId = %s"
        cursor.execute(query, (objet.nom, objet.description, objet.objet_id))

        return objet

    @classmethod
    @with_connection
    def delete(cls, objet_id, **kwargs):
        # get cursor from connection in kwargs
        cursor = get_cursor(kwargs)

        # execute query
        query = "DELETE FROM OBJET WHERE ObjetId = %s"
        cursor.execute(query, (objet_id,))

        return cursor.rowcount > 0
