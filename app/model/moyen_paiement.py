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
        query = "SELECT * FROM MOYEN_PAIEMENT WHERE MoyenPaiementId = %s "
        cursor.execute(query, (moyen_paiement_id,))

        # instantiate all images from cursor
        moyens = []
        for moyen in cursor:
            moyens.append(MoyenPaiement(*moyen))

        return moyens

    @classmethod
    @with_connection
    def select_all(cls, **kwargs):

        # get cursor from connection in kwargs
        cursor = get_cursor(kwargs)

        # execute query
        query = "SELECT * FROM MOYEN_PAIEMENT "
        cursor.execute(query)

        # instantiate all images from cursor
        moyens = []
        for moyen in cursor:
            moyens.append(MoyenPaiement(*moyen))

        return moyens

    @classmethod
    @with_connection
    def insert(cls, moyen_paiement, **kwargs):

        # get cursor from connection in kwargs
        cursor = get_cursor(kwargs)

        # execute query
        query = "INSERT INTO MOYEN_PAIEMENT (MoyenPaiementId, Nom,TaxeDuMoyen) VALUES (%s, %s, %s)"
        cursor.execute(query, (moyen_paiement.moyen_paiement_id, moyen_paiement.nom, moyen_paiement.taxe_du_moyen))

        return moyen_paiement
