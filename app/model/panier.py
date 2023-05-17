from app.database.connector import with_connection, get_cursor
from app.model.jeu import Jeu
from app.model.objet_instance import ObjetInstance


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

        try:
            return Panier(*cursor.fetchone())
        except TypeError:
            return None

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
        query = "INSERT INTO PANIER (Montant) VALUES (%s)"
        cursor.execute(query, (panier.montant,))

        panier.panier_id = cursor.lastrowid


        return panier.panier_id

    @classmethod
    @with_connection
    def update(cls, panier, **kwargs):
        # get cursor from connection in kwargs
        cursor = get_cursor(kwargs)

        # execute query
        query = "UPDATE PANIER SET Montant = %s WHERE PanierId = %s"
        cursor.execute(query, (panier.montant, panier.panier_id,))

        return panier

    @classmethod
    @with_connection
    def delete(cls, panier_id, **kwargs):
        # get cursor from connection in kwargs
        cursor = get_cursor(kwargs)

        # execute query
        query = "DELETE FROM PANIER WHERE PanierId = %s"
        cursor.execute(query, (panier_id,))

        return cursor.rowcount > 0

    ########################
    # Panier-Jeu functions #
    ########################

    @classmethod
    @with_connection
    def get_jeux(cls, panier, **kwargs):
        """
        Get all jeux from a panier
        :param panier: the panier linked to the jeux (must have an id)
        :return: the jeux contained in the panier
        """

        # get cursor from connection in kwargs
        cursor = get_cursor(kwargs)

        # execute query
        query = "SELECT j.* FROM JEU as j, PANIER_JEU as pn WHERE j.GameId = pn.Jeu AND pn.Panier = %s"
        cursor.execute(query, (panier.panier_id,))

        # instantiate all jeux from cursor
        jeux = []
        for jeu in cursor.fetchall():
            jeux.append(Jeu(*jeu))

        return jeux

    @classmethod
    @with_connection
    def add_jeu(cls, panier, jeu, **kwargs):
        """
        Add a jeu to a panier
        :param panier: the exisiting panier (must contain an id)
        :param jeu: the existing jeu to link to panier (must contain an id)
        :return: true if a row has been added, false otherwise
        """

        # get cursor from connection in kwargs
        cursor = get_cursor(kwargs)

        # execute query
        query = "INSERT INTO PANIER_JEU (Panier, Jeu) values (%s, %s)"
        cursor.execute(query, (panier.panier_id, jeu.game_id))

        return cursor.rowcount > 0

    @classmethod
    @with_connection
    def remove_jeu(cls, panier, jeu, **kwargs):
        """
        Remove a jeu to a panier
        :param panier: the exisiting panier (must contain an id)
        :param jeu: the existing jeu to remove from the panier (must contain an id)
        :return: true if a row has been deleted, false otherwise
        """

        # get cursor from connection in kwargs
        cursor = get_cursor(kwargs)

        # execute query
        query = "DELETE FROM PANIER_JEU WHERE Panier = %s AND Jeu = %s"
        cursor.execute(query, (panier.panier_id, jeu.game_id,))

        return cursor.rowcount > 0

    ###########################
    # ObjetInstance functions #
    ###########################

    @classmethod
    @with_connection
    def get_objet_instances(cls, panier, **kwargs):
        """
        Get all objet instances from a panier
        :param panier: the panier linked to objet instances (must have an id)
        :return: the objet instance linked to the panier
        """

        # get cursor from connection in kwargs
        cursor = get_cursor(kwargs)

        # execute query
        query = "SELECT * FROM OBJET_INSTANCE WHERE Panier = %s"
        cursor.execute(query, (panier.panier_id,))

        # instantiate all jeux from cursor
        objet_instances = []
        for objet_instance in cursor.fetchall():
            objet_instances.append(ObjetInstance(*objet_instance))

        return objet_instances
