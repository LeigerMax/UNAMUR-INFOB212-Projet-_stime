from app.database.connector import with_connection, get_cursor


class Game:
    def __init__(self, game_id=None, nom=None, description=None, date_de_sortie=None, prix=None, game_pass=None, developpeur=None, editeur=None, solde=None, est_dlc=None, dlc=None):
        self.game_id = game_id
        self.nom = nom
        self.description = description
        self.date_de_sortie = date_de_sortie
        self.prix = prix
        self.game_pass = game_pass
        self.developpeur = developpeur
        self.editeur = editeur
        self.solde = solde
        self.estDLC = est_dlc
        self.dlc = dlc
    
    @classmethod
    @with_connection
    def select_all_games_shop_page(cls, **kwargs):

        # get cursor from connection in kwargs
        cursor = get_cursor(kwargs)

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

        # get cursor from connection in kwargs
        cursor = get_cursor(kwargs)

        # execute query
        query = "SELECT * FROM JEU WHERE GameId = %s"
        cursor.execute(query, (gameId,))
        game_data = cursor.fetchone()

        #game_data = []
        #game_data.append((game[0], game[1], game[2], game[3], game[4], game[5], game[6]))

        return game_data
