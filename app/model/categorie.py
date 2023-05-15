from app.database.connector import with_connection, get_cursor


class Categorie:
    def __init__(self, nom=None, description=None):
        self.nom = nom
        self.description = description

    @classmethod
    @with_connection
    def select(cls, nom, **kwargs):
        # get cursor from connection in kwargs
        cursor = get_cursor(kwargs)

        # execute query
        query = "SELECT * FROM CATEGORIE WHERE Nom = %s"
        cursor.execute(query, (nom,))

        try:
            return Categorie(*cursor.fetchone())
        except TypeError:
            return None
    
    @classmethod
    @with_connection
    def select_all(cls, **kwargs):
        # get cursor from connection in kwargs
        cursor = get_cursor(kwargs)

        # execute query
        query = "SELECT * FROM CATEGORIE"
        cursor.execute(query)

        # instantiate all users from cursor
        categories = []
        for categorie in cursor.fetchall():
            categories.append(Categorie(*categorie))

        return categories
    
    @classmethod
    @with_connection
    def insert(cls, categorie, **kwargs):
        # get cursor from connection in kwargs
        cursor = get_cursor(kwargs)

        # execute query
        query = "INSERT INTO CATEGORIE (Nom, Description) VALUES (%s, %s)"
        cursor.execute(query, (categorie.nom, categorie.description))

        return categorie
    
    @classmethod
    @with_connection
    def update(cls, categorie, **kwargs):
        # get cursor from connection in kwargs
        cursor = get_cursor(kwargs)

        # execute query
        query = "UPDATE CATEGORIE SET Description = %s WHERE Nom = %s"
        cursor.execute(query, (categorie.description, categorie.nom))

        return categorie
    
    @classmethod
    @with_connection
    def delete(cls, nom, **kwargs):
        # get cursor from connection in kwargs
        cursor = get_cursor(kwargs)

        # execute query
        query = "DELETE FROM CATEGORIE WHERE Nom = %s"
        cursor.execute(query, (nom,))

        return cursor.rowcount > 0
