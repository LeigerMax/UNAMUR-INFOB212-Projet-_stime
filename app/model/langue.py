from app.database.connector import with_connection, get_cursor


class Langue:
    def __init__(self, langue=None, raccourci=None):
        self.langue = langue
        self.raccourci = raccourci

    @classmethod
    @with_connection
    def select(cls, langue, **kwargs):

        # get cursor from connection in kwargs
        cursor = get_cursor(kwargs)

        # execute query
        query = "SELECT * FROM LANGUE WHERE Langue = %s"
        cursor.execute(query, (langue))

        return Langue(*cursor.fetchone())
    
    @classmethod
    @with_connection
    def select_all(cls, **kwargs):

        # get cursor from connection in kwargs
        cursor = get_cursor(kwargs)

        # execute query
        query = "SELECT * FROM LANGUE"
        cursor.execute(query)

        langues = []
        for language in cursor.fetchall():
            langues.append((language[0], language[1]))

        return langues
    
    @classmethod
    @with_connection
    def update(cls, langue, **kwargs):

        # get cursor from connection in kwargs
        cursor = get_cursor(kwargs)

        # execute query
        query = "UPDATE LANGUE SET Raccourci = %s WHERE langue = %s"
        cursor.execute(query, (langue.raccourci, langue.langue))

        return langue

    @classmethod
    @with_connection
    def delete(cls, langue, **kwargs):

        # get cursor from connection in kwargs
        cursor = get_cursor(kwargs)

        # execute query
        query = "DELETE FROM LANGUE WHERE Langue = %s"
        cursor.execute(query, (langue))

        return cursor.rowcount > 0
