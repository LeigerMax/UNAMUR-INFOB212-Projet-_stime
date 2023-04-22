from app.database.connector import with_connection


class Panier:
    def __init__(self, panierId=None,montant=None):
        self.panierId = panierId
        self.montant = montant
    
    @classmethod
    @with_connection
    def select_panier_user(cls,panierId, **kwargs):
        """
        Get panierId in the database
        :return: panierId fetched
        """

        # get connection and cursor
        cnx = kwargs.pop("connection")
        cursor = cnx.cursor()

        # execute query
        query = "SELECT PanierId,Montant FROM PANIER WHERE PanierId = %s"
        cursor.execute(query, (panierId))
        panier = cursor.fetchall()

        panier_list = []
        for produit in panier:
            panier_list.append((produit[0], produit[1]))

        return panier_list
    
