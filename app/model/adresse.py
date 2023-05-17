from app.database.connector import with_connection, get_cursor


class Adresse:
    def __init__(self, adresse_id=None, numero=None, rue=None, ville=None, code_postal=None, pays=None):
        self.adresse_id = adresse_id
        self.numero = numero
        self.rue = rue
        self.ville = ville
        self.code_postal = code_postal
        self.pays = pays

    @classmethod
    @with_connection
    def select(cls, adresse_id, **kwargs):
        # get cursor from connection in kwargs
        cursor = get_cursor(kwargs)

        # execute query
        query = "SELECT * FROM ADRESSE WHERE AdresseId = %s"
        cursor.execute(query, (adresse_id,))

        try:
            return Adresse(*cursor.fetchone())
        except TypeError:
            return None

    @classmethod
    @with_connection
    def select_all(cls, **kwargs):
        # get cursor from connection in kwargs
        cursor = get_cursor(kwargs)

        # execute query
        query = "SELECT * FROM ADRESSE"
        cursor.execute(query)

        # instantiate all adresses from cursor
        adresses = []
        for adresse in cursor.fetchall():
            adresses.append(Adresse(*adresse))

        return adresses
    
    @classmethod
    @with_connection
    def insert(cls, adresse, **kwargs):
        # get cursor from connection in kwargs
        cursor = get_cursor(kwargs)

        # execute query
        query = "INSERT INTO ADRESSE (Numero, Rue, Ville, CodePostal, Pays) VALUES (%s, %s, %s,%s, %s)"
        cursor.execute(query, (adresse.numero, adresse.rue, adresse.ville, adresse.code_postal, adresse.pays))

        # store new id
        adresse.achat_id = cursor.lastrowid

        return adresse.achat_id
        
    
    @classmethod
    @with_connection
    def update(cls, adresse, **kwargs):
        # get cursor from connection in kwargs
        cursor = get_cursor(kwargs)

        # execute query
        query = "UPDATE ADRESSE SET Numero = %s, Rue = %s, Ville = %s, CodePostal = %s, Pays = %s WHERE adresseId = %s"
        cursor.execute(query, (adresse.numero, adresse.rue, adresse.ville, adresse.code_postal, adresse.pays, adresse.adresse_id))

        return adresse
    
    @classmethod
    @with_connection
    def delete(cls, adresse, **kwargs):
        # get cursor from connection in kwargs
        cursor = get_cursor(kwargs)

        # execute query
        query = "DELETE FROM ADRESSE WHERE adresseId = %s"
        cursor.execute(query, (adresse,))

        return cursor.rowcount > 0
