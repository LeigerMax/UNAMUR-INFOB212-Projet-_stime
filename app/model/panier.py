from app.database.connector import with_connection, get_cursor


class Panier:
    def __init__(self, panierId=None, montant=None):
        self.panierId = panierId
        self.montant = montant
    
    @classmethod
    @with_connection
    def select(cls,panierId, **kwargs):
        # get cursor from connection in kwargs
        cursor = get_cursor(kwargs)

        # execute query
        query = "SELECT * FROM PANIER WHERE PanierId = %s "
        cursor.execute(query, (panierId,))

        # instantiate one panier from cursor
        paniers = []
        for panier in cursor:
            paniers.append(Panier(*panier))

        return paniers
    

    @classmethod
    @with_connection
    def select_all(cls, **kwargs):
        # get cursor from connection in kwargs
        cursor = get_cursor(kwargs)

        # execute query
        query = "SELECT * FROM PANIER "
        cursor.execute(query)

         # instantiate all panier from cursor
        paniers = []
        for panier in cursor:
            paniers.append(Panier(*panier))

        return paniers
    
    @classmethod
    @with_connection
    def insert(cls, panier, **kwargs):
        """
        Insert new panier
        :param: panier
        :return: the panier inserted
        """

        # get cursor from connection in kwargs
        cursor = get_cursor(kwargs)

        # execute query
        query = "INSERT INTO PANIER (PanierId, Montant, DateDebutSolde, DateFinSolde) VALUES (%s, %s)"
        cursor.execute(query, (panier.panierId, panier.montant))

        return panier 

    @classmethod
    @with_connection
    def update(cls, panier, **kwargs):
        """
        Update the panier
        :param: panier
        :return: the panier updated
        """

        # get cursor from connection in kwargs
        cursor = get_cursor(kwargs)

        # execute query
        query = "UPDATE PANIER SET Montant = %s WHERE PanierId = %s"
        cursor.execute(query, (panier.motant,panier.url))

        return Panier(*cursor.fetchone())
    

    @classmethod
    @with_connection
    def delete(cls, panier, **kwargs):
        """
        Delete the panier
        :param: the id of the panier
        """

        # get cursor from connection in kwargs
        cursor = get_cursor(kwargs)

        # execute query
        query = "DELETE FROM PANIER WHERE PanierId = %s"
        cursor.execute(query, (panier))
  
    
