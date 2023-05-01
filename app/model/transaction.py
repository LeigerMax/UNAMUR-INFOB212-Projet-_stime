from app.database.connector import with_connection


class Transaction:
    def __init__(self, transactionId=None, dateMiseEnVente=None, dateVente=None, prixVente=None, revendeur=None,acheteur=None,objet=None):
        self.transactionId = transactionId
        self.dateMiseEnVente = dateMiseEnVente
        self.dateVente = dateVente
        self.prixVente = prixVente
        self.revendeur = revendeur
        self.acheteur = acheteur
        self.objet = objet

    @classmethod
    @with_connection
    def select(cls,transactionId, **kwargs):
        # get connection and cursor
        cnx = kwargs.pop("connection")
        cursor = cnx.cursor()

        # execute query
        query = "SELECT * FROM TRANSACTION WHERE TransactionId = %s "
        cursor.execute(query, (transactionId,))

        # instantiate one transaction from cursor
        transactions = []
        for transaction in cursor:
            transactions.append(Transaction(*transaction))

        return transactions
    

    @classmethod
    @with_connection
    def select_all(cls, **kwargs):
        # get connection and cursor
        cnx = kwargs.pop("connection")
        cursor = cnx.cursor()

        # execute query
        query = "SELECT * FROM TRANSACTION "
        cursor.execute(query)

         # instantiate all transactions from cursor
        transactions = []
        for transaction in cursor:
            transactions.append(Transaction(*transaction))

        return transactions
    
    @classmethod
    @with_connection
    def insert(cls, transaction, **kwargs):
        """
        Insert new transaction
        :param: transaction
        :return: the transaction inserted
        """

        # get connection and cursor
        cnx = kwargs.pop("connection")
        cursor = cnx.cursor()

        # execute query
        query = "INSERT INTO TRANSACTION (TransactionId, DateMiseEnVente, DateVente,PrixVente,Revendeur,Acheteur,Objet) VALUES (%s, %s, %s,%s, %s, %s, %s)"
        cursor.execute(query, (transaction.transactionId, transaction.dateMiseEnVente,transaction.dateVente,transaction.prixVente,transaction.revendeur,transaction.acheteur,transaction.objet))

        return transaction   