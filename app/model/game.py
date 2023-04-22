from app.database.connector import with_connection


class Game:
    def __init__(self, gameId=None, nom=None, description=None, dateDeSortie=None, prix=None, estDLC=None, gamePass=None):
        self.gameId = gameId
        self.nom = nom
        self.description = description
        self.dateDeSortie = dateDeSortie
        self.prix = prix
        self.estDLC = estDLC
        self.gamePass = gamePass
    
    @classmethod
    @with_connection
    def select_all_games_shop_page(cls, **kwargs):
        """
        Get all games in the database
        :return: games fetched
        """

        # get connection and cursor
        cnx = kwargs.pop("connection")
        cursor = cnx.cursor()

        # execute query
        query = "SELECT Nom, Description, Prix FROM JEU"
        cursor.execute(query)
        games = cursor.fetchall()

        game_list = []
        for game in games:
            game_list.append((game[0], game[1], game[2]))

        return game_list
    
    @classmethod
    @with_connection
    def select_game_shop_details_page(cls,gameId, **kwargs):
        """
        Get of game in the database
        :return: games fetched
        """

        # get connection and cursor
        cnx = kwargs.pop("connection")
        cursor = cnx.cursor()

        # execute query
        query = "SELECT * FROM JEU WHERE GameId = %s"
        cursor.execute(query, (gameId,))
        game_data = cursor.fetchone()

        #game_data = []
        #game_data.append((game[0], game[1], game[2], game[3], game[4], game[5], game[6]))

        return game_data
