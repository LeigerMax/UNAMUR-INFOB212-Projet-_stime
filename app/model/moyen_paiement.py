from app.database.connector import with_connection, get_cursor


class MoyenPaiement:
    def __init__(self, moyen_paiement_id=None, nom=None, taxe_du_moyen=None):
        self.moyen_paiement_id = moyen_paiement_id
        self.nom = nom
        self.taxe_du_moyen = taxe_du_moyen

    @classmethod
    @with_connection
    def select(cls, moyen_paiement_id, **kwargs):
        # get cursor from connection in kwargs
        cursor = get_cursor(kwargs)

        # execute query
        query = "SELECT * FROM MOYEN_PAIEMENT WHERE MoyenPaiementId = %s"
        cursor.execute(query, (moyen_paiement_id))

        return MoyenPaiement(*cursor.fetchone())

    @classmethod
    @with_connection
    def select_all(cls, **kwargs):
        # get cursor from connection in kwargs
        cursor = get_cursor(kwargs)

        # execute query
        query = "SELECT * FROM MOYEN_PAIEMENT"
        cursor.execute(query)

        # instantiate all moyens de paiement from cursor
        moyens = []
        for moyen in cursor.fetchall():
            moyens.append(MoyenPaiement(*moyen))

        return moyens

    @classmethod
    @with_connection
    def insert(cls, moyen_paiement, **kwargs):
        # get cursor from connection in kwargs
        cursor = get_cursor(kwargs)

        # execute query
        query = "INSERT INTO MOYEN_PAIEMENT (MoyenPaiementId, Nom, TaxeDuMoyen) VALUES (%s, %s, %s)"
        cursor.execute(query, (moyen_paiement.moyen_paiement_id, moyen_paiement.nom, moyen_paiement.taxe_du_moyen))

        # store new id
        moyen_paiement.moyen_paiement_id = cursor.lastrowid

        return moyen_paiement

    @classmethod
    @with_connection
    def update(cls, moyen_paiement, **kwargs):
        # get cursor from connection in kwargs
        cursor = get_cursor(kwargs)

        # execute query
        query = "UPDATE MOYEN_PAIEMENT SET Nom = %s, TaxeDuMoyen = %s WHERE MoyenPaiementId = %s"
        cursor.execute(query, (moyen_paiement.nom, moyen_paiement.taxe_du_moyen, moyen_paiement.moyen_paiement_id))

        return moyen_paiement

    @classmethod
    @with_connection
    def delete(cls, moyen_paiement_id, **kwargs):
        # get cursor from connection in kwargs
        cursor = get_cursor(kwargs)

        # execute query
        query = "DELETE FROM MOYEN_PAIEMENT WHERE MoyenPaiementId = %s"
        cursor.execute(query, (moyen_paiement_id))

        return cursor.rowcount > 0
