from app.database.connector import with_connection

class Moyen_paiement:
    def __init__(self, moyenPaiementId=None,nom=None,taxeDuMoyen=None):
        self.moyenPaiementId = moyenPaiementId
        self.nom = nom
        self.taxeDuMoyen = taxeDuMoyen


    @classmethod
    @with_connection
    def select(cls,moyenPaiementId, **kwargs):
        # get connection and cursor
        cnx = kwargs.pop("connection")
        cursor = cnx.cursor()

        # execute query
        query = "SELECT * FROM MOYEN_PAIEMENT WHERE MoyenPaiementId = %s "
        cursor.execute(query, (moyenPaiementId,))

         # instantiate all images from cursor
        moyens = []
        for moyen in cursor:
            moyens.append(Moyen_paiement(*moyen))

        return moyens
    

    @classmethod
    @with_connection
    def select_all(cls, **kwargs):
        # get connection and cursor
        cnx = kwargs.pop("connection")
        cursor = cnx.cursor()

        # execute query
        query = "SELECT * FROM MOYEN_PAIEMENT "
        cursor.execute(query)

         # instantiate all images from cursor
        moyens = []
        for moyen in cursor:
            moyens.append(Moyen_paiement(*moyen))

        return moyens
    

    @classmethod
    @with_connection
    def insert(cls, moyen_paiement, **kwargs):
        """
        Insert new moyen de paiement
        :param: moyen de paiement
        :return: the moyen de paiement inserted
        """

        # get connection and cursor
        cnx = kwargs.pop("connection")
        cursor = cnx.cursor()

        # execute query
        query = "INSERT INTO MOYEN_PAIEMENT (MoyenPaiementId, Nom,TaxeDuMoyen) VALUES (%s, %s, %s)"
        cursor.execute(query, (moyen_paiement.moyenPaiementId, moyen_paiement.nom,moyen_paiement.taxeDuMoyen ))

        return moyen_paiement