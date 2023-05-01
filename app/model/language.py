from app.database.connector import with_connection, get_cursor


class Language:
    def __init__(self, langue=None, raccourci=None, game_id=None):
        self.langue = langue
        self.raccourci = raccourci
        self.game_id = game_id

    @classmethod
    @with_connection
    def select(cls, langue, **kwargs):

        # get cursor from connection in kwargs
        cursor = get_cursor(kwargs)

        # execute query
        query = "SELECT * FROM LANGUE WHERE Langue = %s"
        cursor.execute(query, (langue,))
        languages = cursor.fetchall()

        language_list = []
        for language in languages:
            language_list.append((language[0], language[1]))

        return language_list
    
    @classmethod
    @with_connection
    def select_all(cls, **kwargs):

        # get cursor from connection in kwargs
        cursor = get_cursor(kwargs)

        # execute query
        query = "SELECT * FROM LANGUE"
        cursor.execute(query)
        languages = cursor.fetchall()

        language_list = []
        for language in languages:
            language_list.append((language[0], language[1]))

        return language_list
    
    @classmethod
    @with_connection
    def update(cls, langue, **kwargs):

        # get cursor from connection in kwargs
        cursor = get_cursor(kwargs)

        # execute query
        query = "UPDATE LANGUE SET Raccourci = %s WHERE langue = %s"
        cursor.execute(query, (langue.raccourci, langue.langue))

        return Language(*cursor.fetchone())

    @classmethod
    @with_connection
    def delete(cls, langue, **kwargs):

        # get cursor from connection in kwargs
        cursor = get_cursor(kwargs)

        # execute query
        query = "DELETE FROM LANGUE WHERE Langue = %s"
        cursor.execute(query, (langue))
