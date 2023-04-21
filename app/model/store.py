from app.database.connector import with_connection


class Store:
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
    def select(cls, **kwargs):
        pass

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
    def create(cls, user):
        pass

    @classmethod
    def update(cls, user):
        pass

    @classmethod
    def delete(cls, user):
        pass
