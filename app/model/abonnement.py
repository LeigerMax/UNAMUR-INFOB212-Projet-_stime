from app.database.connector import with_connection, get_cursor


class Abonnement:
    def __init__(self, type=None, prix=None):
        self.type = type
        self.prix = prix

    @classmethod
    @with_connection
    def select(cls, type, **kwargs):
        # get cursor from connection in kwargs
        cursor = get_cursor(kwargs)

        # execute query
        query = "SELECT * FROM ABONNEMENT WHERE Type = %s"
        cursor.execute(query, (type,))

        try:
            return Abonnement(*cursor.fetchone())
        except TypeError:
            return None

    @classmethod
    @with_connection
    def select_all(cls, **kwargs):
        # get cursor from connection in kwargs
        cursor = get_cursor(kwargs)

        # execute query
        query = "SELECT * FROM ABONNEMENT"
        cursor.execute(query)

        # instantiate all abonnements from cursor
        abonnements = []
        for abonnement in cursor.fetchall():
            abonnements.append(Abonnement(*abonnement))

        return abonnements

    @classmethod
    @with_connection
    def insert(cls, abonnement, **kwargs):
        # get cursor from connection in kwargs
        cursor = get_cursor(kwargs)

        # execute query
        query = "INSERT INTO ABONNEMENT (Type, Prix) VALUES (%s, %s)"
        cursor.execute(query, (abonnement.type, abonnement.prix,))

        return abonnement

    @classmethod
    @with_connection
    def update(cls, abonnement, **kwargs):
        # get cursor from connection in kwargs
        cursor = get_cursor(kwargs)

        # execute query
        query = "UPDATE ABONNEMENT SET Prix = %s"
        cursor.execute(query, (abonnement.prix,))

        return abonnement

    @classmethod
    @with_connection
    def delete(cls, type, **kwargs):
        # get cursor from connection in kwargs
        cursor = get_cursor(kwargs)

        # execute query
        query = "DELETE FROM ABONNEMENT WHERE Type = %s"
        cursor.execute(query, (type,))

        return cursor.rowcount > 0
