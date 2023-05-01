from app.database.connector import with_connection, get_cursor


class Adresse:
    def __init__(self, adresseId=None, numero=None, rue=None, ville=None, codePostal=None, pays=None):
        self.adresseId = adresseId
        self.numero = numero
        self.rue = rue
        self.ville = ville
        self.codePostal = codePostal
        self.pays = pays

    @classmethod
    @with_connection
    def select(cls,adresseId, **kwargs):
        # get cursor from connection in kwargs
        cursor = get_cursor(kwargs)

        # execute query
        query = "SELECT * FROM ADRESSE WHERE AdresseId = %s "
        cursor.execute(query, (adresseId,))

        # instantiate one adresse from cursor
        adresses = []
        for adresse in cursor:
            adresses.append(Adresse(*adresse))

        return adresses
    

    @classmethod
    @with_connection
    def select_all(cls, **kwargs):
        # get cursor from connection in kwargs
        cursor = get_cursor(kwargs)

        # execute query
        query = "SELECT * FROM ADRESSE "
        cursor.execute(query)

         # instantiate all adresses from cursor
        adresses = []
        for adresse in cursor:
            adresses.append(Adresse(*adresse))

        return adresses
    
    @classmethod
    @with_connection
    def insert(cls, adresse, **kwargs):
        """
        Insert new adresse
        :param: adresse
        :return: the adresse inserted
        """

        # get cursor from connection in kwargs
        cursor = get_cursor(kwargs)

        # execute query
        query = "INSERT INTO ADRESSE (AdresseId, Numero,Rue,Ville,CodePostal,Pays) VALUES (%s, %s, %s,%s, %s, %s)"
        cursor.execute(query, (adresse.adresseId, adresse.numero,adresse.rue,adresse.ville,adresse.codePostal,adresse.pays))

        return adresse
    
    @classmethod
    @with_connection
    def update(cls, adresse, **kwargs):
        """
        Update the adresse
        :param: adresse
        :return: the adresse updated
        """

        # get cursor from connection in kwargs
        cursor = get_cursor(kwargs)

        # execute query
        query = "UPDATE ADRESSE SET Numero = %s,Rue = %s ,Ville = %s ,CodePostal = %s,Pays = %s WHERE adresseId = %s"
        cursor.execute(query, (adresse.numero,adresse.rue,adresse.ville,adresse.codePostal, adresse.pays, adresse.adresseId))

        return Adresse(*cursor.fetchone())
    
    @classmethod
    @with_connection
    def delete(cls, adresse, **kwargs):
        """
        Delete the adresse
        :param: the id of the adresse
        """

        # get cursor from connection in kwargs
        cursor = get_cursor(kwargs)

        # execute query
        query = "DELETE FROM ADRESSE WHERE adresseId = %s"
        cursor.execute(query, (adresse))