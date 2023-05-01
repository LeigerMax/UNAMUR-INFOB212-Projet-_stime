from app.database.connector import with_connection, get_cursor


class Panier:
    def __init__(self, panier_id=None, montant=None):
        self.panier_id = panier_id
        self.montant = montant
    
    @classmethod
    @with_connection
    def select(cls, panier_id, **kwargs):
        # get cursor from connection in kwargs
        cursor = get_cursor(kwargs)

        # execute query
        query = "SELECT * FROM PANIER WHERE PanierId = %s"
        cursor.execute(query, (panier_id,))

        return Panier(*cursor.fetchone())

    @classmethod
    @with_connection
    def select_all(cls, **kwargs):
        # get cursor from connection in kwargs
        cursor = get_cursor(kwargs)

        # execute query
        query = "SELECT * FROM PANIER"
        cursor.execute(query)

        # instantiate all panier from cursor
        paniers = []
        for panier in cursor.fetchall():
            paniers.append(Panier(*panier))

        return paniers
    
    @classmethod
    @with_connection
    def insert(cls, panier, **kwargs):
        # get cursor from connection in kwargs
        cursor = get_cursor(kwargs)

        # execute query
        query = "INSERT INTO PANIER (Montant) VALUES (%s, %s)"
        cursor.execute(query, (panier.montant))

        return panier 

    @classmethod
    @with_connection
    def update(cls, panier, **kwargs):
        # get cursor from connection in kwargs
        cursor = get_cursor(kwargs)

        # execute query
        query = "UPDATE PANIER SET Montant = %s WHERE PanierId = %s"
        cursor.execute(query, (panier.motant, panier.panier_id))

        return panier

    @classmethod
    @with_connection
    def delete(cls, panier_id, **kwargs):
        # get cursor from connection in kwargs
        cursor = get_cursor(kwargs)

        # execute query
        query = "DELETE FROM PANIER WHERE PanierId = %s"
        cursor.execute(query, (panier_id))

        return cursor.rowcount > 0
