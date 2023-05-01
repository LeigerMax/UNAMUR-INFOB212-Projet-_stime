from app.database.connector import with_connection, get_cursor


class Achat:
    def __init__(self, achatId=None, montantTotal=None, dateAchat=None, utilisateur=None, moyenPaiement=None,panier=None):
        self.achatId = achatId
        self.montantTotal = montantTotal
        self.dateAchat = dateAchat
        self.utilisateur = utilisateur
        self.moyenPaiement = moyenPaiement
        self.panier = panier


    @classmethod
    @with_connection
    def select(cls,achatId, **kwargs):

        # get cursor from connection in kwargs
        cursor = get_cursor(kwargs)

        # execute query
        query = "SELECT * FROM ACHAT WHERE AchatId = %s "
        cursor.execute(query, (achatId,))

        # instantiate one evaluation from cursor
        achats = []
        for achat in cursor:
            achats.append(Achat(*achat))

        return achats
    

    @classmethod
    @with_connection
    def select_all(cls, **kwargs):

        # get cursor from connection in kwargs
        cursor = get_cursor(kwargs)

        # execute query
        query = "SELECT * FROM ACHAT "
        cursor.execute(query)

         # instantiate all achats from cursor
        achats = []
        for achat in cursor:
            achats.append(Achat(*achat))

        return achats
    
    @classmethod
    @with_connection
    def insert(cls, achat, **kwargs):
        """
        Insert new achat
        :param: achat
        :return: the achat inserted
        """

        # get cursor from connection in kwargs
        cursor = get_cursor(kwargs)

        # execute query
        query = "INSERT INTO ACHAT (AchatId, MontantTotal,DateAchat,Utilisateur,MoyenPaiement,Panier) VALUES (%s, %s, %s,%s, %s, %s)"
        cursor.execute(query, (achat.achatId, achat.montantTotal,achat.dateAchat,achat.utilisateur,achat.moyenPaiement,achat.panier))

        return achat
    
    @classmethod
    @with_connection
    def update(cls, achat, **kwargs):
        """
        Update the achat
        :param: achat
        :return: the achat updated
        """

        # get cursor from connection in kwargs
        cursor = get_cursor(kwargs)

        # execute query
        query = "UPDATE ACHAT SET MontantTotal = %s,DateAchat = %s ,Utilisateur = %s ,MoyenPaiement = %s,Panier = %s WHERE AchatId = %s"
        cursor.execute(query, (achat.montantTotal,achat.dateAchat,achat.utilisateur,achat.moyenPaiement, achat.panier, achat.achatId))

        return Achat(*cursor.fetchone())
    
    @classmethod
    @with_connection
    def delete(cls, achat, **kwargs):
        """
        Delete the achat
        :param: the id of the achat
        """

        # get cursor from connection in kwargs
        cursor = get_cursor(kwargs)

        # execute query
        query = "DELETE FROM ACHAT WHERE AchatId = %s"
        cursor.execute(query, (achat))