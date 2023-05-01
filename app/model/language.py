from app.database.connector import with_connection


class Language:
    def __init__(self,langue=None, raccourci=None,gameId=None):
        self.langue = langue
        self.raccourci = raccourci
        self.gameId = gameId
    

    @classmethod
    @with_connection
    def select(cls,langue, **kwargs):
        """
        Get one langue from
        :param nom: the name of the langue to fetch
        :return: the langue fetched
        """

        # get connection and cursor
        cnx = kwargs.pop("connection")
        cursor = cnx.cursor()

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
        """
        Get language all games in the database
        :return: language fetched
        """

        # get connection and cursor
        cnx = kwargs.pop("connection")
        cursor = cnx.cursor()

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
        """
        Update the language
        :param: language
        :return: the language updated
        """

        # get connection and cursor
        cnx = kwargs.pop("connection")
        cursor = cnx.cursor()

        # execute query
        query = "UPDATE LANGUE SET Raccourci = %s WHERE langue = %s"
        cursor.execute(query, (langue.raccourci,langue.langue))

        return Language(*cursor.fetchone())
    

    @classmethod
    @with_connection
    def delete(cls, langue, **kwargs):
        """
        Delete the langue
        :param: the id of the langue
        """

        # get connection and cursor
        cnx = kwargs.pop("connection")
        cursor = cnx.cursor()

        # execute query
        query = "DELETE FROM LANGUE WHERE Langue = %s"
        cursor.execute(query, (langue))

