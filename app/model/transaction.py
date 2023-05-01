from app.database.connector import with_connection, get_cursor


class Transaction:
    def __init__(self, transaction_id=None, date_mise_en_vente=None, date_vente=None, prix_vente=None, revendeur=None, acheteur=None, objet=None):
        self.transaction_id = transaction_id
        self.date_mise_en_vente = date_mise_en_vente
        self.date_vente = date_vente
        self.prix_vente = prix_vente
        self.revendeur = revendeur
        self.acheteur = acheteur
        self.objet = objet

    @classmethod
    @with_connection
    def select(cls, transaction_id, **kwargs):
        # get cursor from connection in kwargs
        cursor = get_cursor(kwargs)

        # execute query
        query = "SELECT * FROM TRANSACTION WHERE TransactionId = %s"
        cursor.execute(query, (transaction_id))

        return Transaction(*cursor.fetchone())

    @classmethod
    @with_connection
    def select_all(cls, **kwargs):
        # get cursor from connection in kwargs
        cursor = get_cursor(kwargs)

        # execute query
        query = "SELECT * FROM TRANSACTION"
        cursor.execute(query)

        # instantiate all transactions from cursor
        transactions = []
        for transaction in cursor.fetchall():
            transactions.append(Transaction(*transaction))

        return transactions
    
    @classmethod
    @with_connection
    def insert(cls, transaction, **kwargs):
        # get cursor from connection in kwargs
        cursor = get_cursor(kwargs)

        # execute query
        query = "INSERT INTO TRANSACTION (DateMiseEnVente, DateVente, PrixVente, Revendeur, Acheteur, Objet) VALUES (%s, %s, %s, %s, %s, %s)"
        cursor.execute(query, (transaction.date_mise_en_vente, transaction.date_vente, transaction.prix_vente, transaction.revendeur, transaction.acheteur, transaction.objet))

        # store new id
        transaction.transaction_id = cursor.lastrowid

        return transaction

    @classmethod
    @with_connection
    def update(cls, transaction, **kwargs):
        # get cursor from connection in kwargs
        cursor = get_cursor(kwargs)

        # execute query
        query = "UPDATE TRANSACTION SET DateMiseEnVente = %s, DateVente = %s, PrixVente = %s, Revendeur = %s, Acheteur = %s, Objet = %s WHERE TransactionId = %s"
        cursor.execute(query, (transaction.date_mise_en_vente, transaction.date_vente, transaction.prix_vente, transaction.revendeur, transaction.acheteur, transaction.objet, transaction.transaction_id))

        return transaction

    @classmethod
    @with_connection
    def delete(cls, transaction_id, **kwargs):
        # get cursor from connection in kwargs
        cursor = get_cursor(kwargs)

        # execute query
        query = "DELETE FROM TRANSACTION WHERE TransactionId = %s"
        cursor.execute(query, (transaction_id))

        return cursor.rowcount > 0
