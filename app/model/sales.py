from app.database.connector import with_connection, get_cursor


class Sales:
    def __init__(self, montant=None, annee=None, mois=None):
        self.montant = montant
        self.annee = annee
        self.mois = mois

    @classmethod
    @with_connection
    def annual_sales(cls, **kwargs):
        # get cursor from connection in kwargs
        cursor = get_cursor(kwargs)

        # execute query
        query = "SELECT * FROM CA_VENTE"
        cursor.execute(query)

        # instantiate all sales from cursor
        sales_list = []
        for sales in cursor.fetchall():
            sales_list.append(Sales(*sales))

        return sales_list

    @classmethod
    @with_connection
    def monthly_sales(cls, **kwargs):
        # get cursor from connection in kwargs
        cursor = get_cursor(kwargs)

        # execute query
        query = "SELECT * FROM CA_VENTE_MENSUEL"
        cursor.execute(query)

        # instantiate all sales from cursor
        sales_list = []
        for sales in cursor.fetchall():
            sales_list.append(Sales(*sales))

        return sales_list
