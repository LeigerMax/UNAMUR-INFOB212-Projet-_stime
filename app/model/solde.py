from app.database.connector import with_connection, get_cursor


class Solde:
    def __init__(self, solde_id=None, taux_solde=None, date_debut_solde=None, date_fin_solde=None):
        self.solde_id = solde_id
        self.taux_solde = taux_solde
        self.date_debut_solde = date_debut_solde
        self.date_fin_solde = date_fin_solde

    @classmethod
    @with_connection
    def select(cls, solde_id, **kwargs):

        # get cursor from connection in kwargs
        cursor = get_cursor(kwargs)

        # execute query
        query = "SELECT * FROM SOLDE WHERE SoldeId = %s "
        cursor.execute(query, (solde_id,))

        return Solde(*cursor.fetchone())

    @classmethod
    @with_connection
    def select_all(cls, **kwargs):

        # get cursor from connection in kwargs
        cursor = get_cursor(kwargs)

        # execute query
        query = "SELECT * FROM SOLDE"
        cursor.execute(query)

        # instantiate all transactions from cursor
        soldes = []
        for solde in cursor.fetchall():
            soldes.append(Solde(*solde))

        return soldes
    
    @classmethod
    @with_connection
    def insert(cls, solde, **kwargs):

        # get cursor from connection in kwargs
        cursor = get_cursor(kwargs)

        # execute query
        query = "INSERT INTO SOLDE (TauxSolde, DateDebutSolde, DateFinSolde) VALUES (%s, %s, %s)"
        cursor.execute(query, (solde.taux_solde, solde.date_debut_solde, solde.date_fin_solde))

        # store new id
        solde.objet_id = cursor.lastrowid

        return solde
    
    @classmethod
    @with_connection
    def update(cls, solde, **kwargs):

        # get cursor from connection in kwargs
        cursor = get_cursor(kwargs)

        # execute query
        query = "UPDATE SOLDE SET TauxSolde = %s, DateDebutSolde = %s, DateFinSolde = %s WHERE SoldeId = %s"
        cursor.execute(query, (solde.taux_solde, solde.date_debut_solde, solde.date_fin_solde, solde.solde_id))

        return solde

    @classmethod
    @with_connection
    def delete(cls, solde_id, **kwargs):

        # get cursor from connection in kwargs
        cursor = get_cursor(kwargs)

        # execute query
        query = "DELETE FROM SOLDE WHERE SoldeId = %s"
        cursor.execute(query, (solde_id))

        return cursor.rowcount > 0
