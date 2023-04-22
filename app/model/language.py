from app.database.connector import with_connection


class Language:
    def __init__(self, gameId=None):
        self.gameId = gameId
    
    @classmethod
    @with_connection
    def select(cls, **kwargs):
        pass

    @classmethod
    @with_connection
    def select_language_of_game(cls,gameId, **kwargs):
        """
        Get language of game in the database
        :return: games fetched
        """

        # get connection and cursor
        cnx = kwargs.pop("connection")
        cursor = cnx.cursor()

        # execute query
        query = "SELECT Langue,Raccourci FROM LANGUE_JEU WHERE GameId = %s"
        cursor.execute(query, (gameId,))
        languages = cursor.fetchall()

        language_list = []
        for language in languages:
            language_list.append((language[0], language[1]))

        return language_list
    
    @classmethod
    @with_connection
    def select_language_all_games(cls, **kwargs):
        """
        Get language all games in the database
        :return: games fetched
        """

        # get connection and cursor
        cnx = kwargs.pop("connection")
        cursor = cnx.cursor()

        # execute query
        query = "SELECT Langue,Raccourci FROM LANGUE_JEU"
        cursor.execute(query)
        languages = cursor.fetchall()

        language_list = []
        for language in languages:
            language_list.append((language[0], language[1]))

        return language_list

    @classmethod
    def create(cls, user):
        pass

    @classmethod
    def update(cls, user):
        pass

    @classmethod
    def delete(cls, user):
        pass
