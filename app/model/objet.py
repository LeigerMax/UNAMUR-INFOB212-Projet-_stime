from app.database.connector import with_connection, get_cursor


class Objet:
    def __init__(self, objetId=None, nom=None, description=None, gameId=None):
        self.objetId = objetId
        self.nom = nom
        self.description = description
        self.gameId = gameId
        
    @classmethod
    @with_connection
    def select(cls,objetId, **kwargs):
        # get cursor from connection in kwargs
        cursor = get_cursor(kwargs)

        # execute query
        query = "SELECT * FROM OBJET WHERE ObjetId = %s "
        cursor.execute(query, (objetId,))

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
        """
        Insert new objet
        :param: objet
        :return: the objet inserted
        """

        # get cursor from connection in kwargs
        cursor = get_cursor(kwargs)

        # execute query
        query = "INSERT INTO OBJET (ObjetId, Nom, Description, Jeu) VALUES (%s, %s, %s, %s)"
        cursor.execute(query, (objet.objetId, objet.nom, objet.description, objet.jeu))

        return objet   