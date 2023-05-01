from app.database.connector import with_connection, get_cursor


class Objet:
    def __init__(self, objet_id=None, nom=None, description=None, game_id=None):
        self.objetId = objet_id
        self.nom = nom
        self.description = description
        self.gameId = game_id
        
    @classmethod
    @with_connection
    def select(cls, objet_id, **kwargs):
        # get cursor from connection in kwargs
        cursor = get_cursor(kwargs)

        # execute query
        query = "SELECT * FROM OBJET WHERE ObjetId = %s "
        cursor.execute(query, (objet_id,))

        # instantiate one objet from cursor
        objects = []
        for objet in cursor:
            objects.append(Objet(*objet))

        return objects

    @classmethod
    @with_connection
    def select_all(cls, **kwargs):
        # get cursor from connection in kwargs
        cursor = get_cursor(kwargs)

        # execute query
        query = "SELECT * FROM OBJET "
        cursor.execute(query)

        # instantiate all objet from cursor
        objets = []
        for objet in cursor:
            objets.append(Objet(*objet))

        return objets
    
    @classmethod
    @with_connection
    def insert(cls, objet, **kwargs):
        # get cursor from connection in kwargs
        cursor = get_cursor(kwargs)

        # execute query
        query = "INSERT INTO OBJET (ObjetId, Nom, Description, Jeu) VALUES (%s, %s, %s, %s)"
        cursor.execute(query, (objet.objetId, objet.nom, objet.description, objet.jeu))

        return objet
