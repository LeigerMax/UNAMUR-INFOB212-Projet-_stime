from app.database.connector import with_connection, get_cursor


class Achat:
    def __init__(self, achat_id=None, montant_total=None, date_achat=None, utilisateur=None, moyen_paiement=None, panier=None):
        self.achat_id = achat_id
        self.montant_total = montant_total
        self.date_achat = date_achat
        self.utilisateur = utilisateur
        self.moyen_paiement = moyen_paiement
        self.panier = panier

    @classmethod
    @with_connection
    def select(cls, achat_id, **kwargs):

        # get cursor from connection in kwargs
        cursor = get_cursor(kwargs)

        # execute query
        query = "SELECT * FROM ACHAT WHERE AchatId = %s"
        cursor.execute(query, (achat_id))

        return Achat(*cursor.fetchone())

    @classmethod
    @with_connection
    def select_all(cls, **kwargs):

        # get cursor from connection in kwargs
        cursor = get_cursor(kwargs)

        # execute query
        query = "SELECT * FROM ACHAT"
        cursor.execute(query)

        # instantiate all achats from cursor
        achats = []
        for achat in cursor.fetchall():
            achats.append(Achat(*achat))

        return achats
    
    @classmethod
    @with_connection
    def insert(cls, achat, **kwargs):

        # get cursor from connection in kwargs
        cursor = get_cursor(kwargs)

        # execute query
        query = "INSERT INTO ACHAT (MontantTotal, DateAchat, Utilisateur, MoyenPaiement, Panier) VALUES (%s, %s, %s, %s, %s, %s)"
        cursor.execute(query, (achat.montant_total, achat.date_achat, achat.utilisateur, achat.moyen_paiement, achat.panier))

        # store new id
        achat.achat_id = cursor.lastrowid

        return achat
    
    @classmethod
    @with_connection
    def update(cls, achat, **kwargs):

        # get cursor from connection in kwargs
        cursor = get_cursor(kwargs)

        # execute query
        query = "UPDATE ACHAT SET MontantTotal = %s, DateAchat = %s, Utilisateur = %s, MoyenPaiement = %s, Panier = %s WHERE AchatId = %s"
        cursor.execute(query, (achat.montant_total, achat.date_achat, achat.utilisateur, achat.moyen_paiement, achat.panier, achat.achat_id))

        return achat
    
    @classmethod
    @with_connection
    def delete(cls, achat, **kwargs):

        # get cursor from connection in kwargs
        cursor = get_cursor(kwargs)

        # execute query
        query = "DELETE FROM ACHAT WHERE AchatId = %s"
        cursor.execute(query, (achat))

        return cursor.rowcount > 0
