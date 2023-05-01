from app.database.connector import with_connection, get_cursor


class Entreprise:
    def __init__(self, numSiret=None, nom=None, description=None, adresseWeb=None, estBoiteDev=None, estEditeur=None):
        self.numSiret = numSiret
        self.nom = nom
        self.description = description
        self.adresseWeb = adresseWeb
        self.estBoiteDev = estBoiteDev
        self.estEditeur = estEditeur


    @classmethod
    @with_connection
    def select(cls,numSiret, **kwargs):
        # get cursor from connection in kwargs
        cursor = get_cursor(kwargs)

        # execute query
        query = "SELECT * FROM ENTREPRISE WHERE NumSiret = %s "
        cursor.execute(query, (numSiret,))

        # instantiate one evaluation from cursor
        entreprises = []
        for entreprise in cursor:
            entreprises.append(Entreprise(*entreprise))

        return entreprises
    

    @classmethod
    @with_connection
    def select_all(cls, **kwargs):
        # get cursor from connection in kwargs
        cursor = get_cursor(kwargs)

        # execute query
        query = "SELECT * FROM ENTREPRISE "
        cursor.execute(query)

         # instantiate all entreprises from cursor
        entreprises = []
        for entreprise in cursor:
            entreprises.append(Entreprise(*entreprise))

        return entreprises
    
    @classmethod
    @with_connection
    def insert(cls, entreprise, **kwargs):
        """
        Insert new entreprise
        :param: entreprise
        :return: the entreprise inserted
        """

        # get cursor from connection in kwargs
        cursor = get_cursor(kwargs)

        # execute query
        query = "INSERT INTO ENTREPRISE (NumSiret, Nom, Description,AdresseWeb,EstBoiteDev,EstEditeur) VALUES (%s, %s, %s,%s, %s, %s)"
        cursor.execute(query, (entreprise.numSiret, entreprise.nom,entreprise.description,entreprise.adresseWeb,entreprise.estBoiteDev,entreprise.estEditeur))

        return entreprise
    
    @classmethod
    @with_connection
    def update(cls, entreprise, **kwargs):
        """
        Update the entreprise
        :param: entreprise
        :return: the entreprise updated
        """

        # get cursor from connection in kwargs
        cursor = get_cursor(kwargs)

        # execute query
        query = "UPDATE ENTREPRISE SET Nom = %s ,Description = %s ,AdresseWeb = %s,EstBoiteDev = %s, EstEditeur = %s WHERE NumSiret = %s"
        cursor.execute(query, (entreprise.nom,entreprise.description,entreprise.adresseWeb,entreprise.estBoiteDev, entreprise.estEditeur, entreprise.numSiret))

        return Entreprise(*cursor.fetchone())
    
    @classmethod
    @with_connection
    def delete(cls, entreprise, **kwargs):
        """
        Delete the entreprise
        :param: the id of the entreprise
        """

        # get cursor from connection in kwargs
        cursor = get_cursor(kwargs)

        # execute query
        query = "DELETE FROM ENTREPRISE WHERE NumSiret = %s"
        cursor.execute(query, (entreprise))