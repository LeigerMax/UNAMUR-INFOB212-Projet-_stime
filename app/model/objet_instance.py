from app.database.connector import with_connection, get_cursor


class ObjetInstance:
    def __init__(self, id=None, date_obtention=None, possesseur=None, objet=None, panier=None):
        self.id = id
        self.date_obtention = date_obtention
        self.possesseur = possesseur
        self.objet = objet
        self.panier = panier

    @classmethod
    @with_connection
    def select(cls, objet_instance_id, **kwargs):
        # get cursor from connection in kwargs
        cursor = get_cursor(kwargs)

        # execute query
        query = "SELECT * FROM OBJET_INSTANCE WHERE Id = %s"
        cursor.execute(query, (objet_instance_id))

        return ObjetInstance(*cursor.fetchone())

    @classmethod
    @with_connection
    def select_all(cls, **kwargs):
        # get cursor from connection in kwargs
        cursor = get_cursor(kwargs)

        # execute query
        query = "SELECT * FROM OBJET_INSTANCE"
        cursor.execute(query)

        # instantiate all objet instances from cursor
        objet_instances = []
        for instance in cursor.fetchall():
            objet_instances.append(ObjetInstance(*instance))

        return objet_instances

    @classmethod
    @with_connection
    def insert(cls, objet_instance, **kwargs):
        # get cursor from connection in kwargs
        cursor = get_cursor(kwargs)

        # execute query
        query = "INSERT INTO OBJET_INSTANCE (DateObtention, Possesseur, Objet, Panier) VALUES (%s, %s, %s, %s)"
        cursor.execute(query, (objet_instance.date_obtention, objet_instance.possesseur, objet_instance.objet, objet_instance.panier))

        # store new id
        objet_instance.id = cursor.lastrowid

        return objet_instance

    @classmethod
    @with_connection
    def update(cls, objet_instance, **kwargs):
        # get cursor from connection in kwargs
        cursor = get_cursor(kwargs)

        # execute query
        query = "UPDATE OBJET_INSTANCE SET DateObtention = %s, Possesseur = %s, Objet = %s, Panier = %s WHERE PanierId = %s"
        cursor.execute(query, (objet_instance.date_obtention, objet_instance.possesseur, objet_instance.objet, objet_instance.panier, objet_instance.id))

        return objet_instance

    @classmethod
    @with_connection
    def delete(cls, objet_instance_id, **kwargs):
        # get cursor from connection in kwargs
        cursor = get_cursor(kwargs)

        # execute query
        query = "DELETE FROM OBJET_INSTANCE WHERE Id = %s"
        cursor.execute(query, (objet_instance_id))

        return cursor.rowcount > 0
