from app.database.connector import with_connection, get_cursor


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

        return Entreprise(*cursor.fetchone())

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
