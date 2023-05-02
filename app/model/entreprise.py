from app.database.connector import with_connection, get_cursor
from app.model.adresse import Adresse


class Entreprise:
    def __init__(self, num_siret=None, nom=None, description=None, adresse_web=None, est_boite_dev=None, est_editeur=None):
        self.num_siret = num_siret
        self.nom = nom
        self.description = description
        self.adresse_web = adresse_web
        self.est_boite_dev = est_boite_dev
        self.est_editeur = est_editeur

    @classmethod
    @with_connection
    def select(cls, num_siret, **kwargs):
        # get cursor from connection in kwargs
        cursor = get_cursor(kwargs)

        # execute query
        query = "SELECT * FROM ENTREPRISE WHERE NumSiret = %s "
        cursor.execute(query, (num_siret))

        try:
            return Entreprise(*cursor.fetchone())
        except TypeError:
            return None

    @classmethod
    @with_connection
    def select_all(cls, **kwargs):
        # get cursor from connection in kwargs
        cursor = get_cursor(kwargs)

        # execute query
        query = "SELECT * FROM ENTREPRISE"
        cursor.execute(query)

        # instantiate all entreprises from cursor
        entreprises = []
        for entreprise in cursor.fetchall():
            entreprises.append(Entreprise(*entreprise))

        return entreprises
    
    @classmethod
    @with_connection
    def insert(cls, entreprise, **kwargs):
        # get cursor from connection in kwargs
        cursor = get_cursor(kwargs)

        # execute query
        query = "INSERT INTO ENTREPRISE (NumSiret, Nom, Description, AdresseWeb, EstBoiteDev, EstEditeur) VALUES (%s, %s, %s, %s, %s, %s)"
        cursor.execute(query, (entreprise.num_siret, entreprise.nom, entreprise.description, entreprise.adresse_web, entreprise.est_boite_dev, entreprise.est_editeur))

        return entreprise
    
    @classmethod
    @with_connection
    def update(cls, entreprise, **kwargs):
        # get cursor from connection in kwargs
        cursor = get_cursor(kwargs)

        # execute query
        query = "UPDATE ENTREPRISE SET Nom = %s, Description = %s, AdresseWeb = %s, EstBoiteDev = %s, EstEditeur = %s WHERE NumSiret = %s"
        cursor.execute(query, (entreprise.nom, entreprise.description, entreprise.adresse_web, entreprise.est_boite_dev, entreprise.est_editeur, entreprise.num_siret))

        return entreprise
    
    @classmethod
    @with_connection
    def delete(cls, entreprise, **kwargs):
        # get cursor from connection in kwargs
        cursor = get_cursor(kwargs)

        # execute query
        query = "DELETE FROM ENTREPRISE WHERE NumSiret = %s"
        cursor.execute(query, (entreprise))

        return cursor.rowcount > 0

    ################################
    # Entreprise-Adresse functions #
    ################################

    @classmethod
    @with_connection
    def get_adresses(cls, entreprise, **kwargs):
        """
        Get all adresses from an entreprise
        :param entreprise: the entreprise linked to the adresses (must have an id)
        :return: the adresses of the entreprise
        """

        # get cursor from connection in kwargs
        cursor = get_cursor(kwargs)

        # execute query
        query = "SELECT a.* FROM ADRESSE as a, ENTREPRISE_ADRESSE as ea WHERE a.AdresseId = ea.Adresse AND ea.Entreprise = %s"
        cursor.execute(query, (entreprise.num_siret))

        # instantiate all adresses from cursor
        adresses = []
        for adresse in cursor.fetchall():
            adresses.append(Adresse(*adresse))

        return adresses

    @classmethod
    @with_connection
    def add_adresse(cls, entreprise, adresse, **kwargs):
        """
        Add an adresse to an entreprise
        :param entreprise: the exisiting entreprise (must contain an id)
        :param adresse: the existing adresse to link to entreprise (must contain an id)
        :return: true if a row has been added, false otherwise
        """

        # get cursor from connection in kwargs
        cursor = get_cursor(kwargs)

        # execute query
        query = "INSERT INTO ENTREPRISE_ADRESSE (Entreprise, Adresse) values (%s, %s)"
        cursor.execute(query, (entreprise.num_siret, adresse.adresse_id))

        return cursor.rowcount > 0

    @classmethod
    @with_connection
    def remove_adresse(cls, entreprise, adresse, **kwargs):
        """
        Remove an adresse to an entreprise
        :param entreprise: the exisiting entreprise (must contain an id)
        :param adresse: the existing adresse to remove from the entreprise (must contain an id)
        :return: true if a row has been deleted, false otherwise
        """

        # get cursor from connection in kwargs
        cursor = get_cursor(kwargs)

        # execute query
        query = "DELETE FROM ENTREPRISE_ADRESSE WHERE Entreprise = %s AND Adresse = %s"
        cursor.execute(query, (entreprise.num_siret, adresse.adresse_id))

        return cursor.rowcount > 0
