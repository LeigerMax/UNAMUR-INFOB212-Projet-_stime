from app.database.connector import with_connection, get_cursor


class Solde:
    def __init__(self, soldeId=None,tauxSolde=None,dateDebutSolde=None,dateFinSolde=None):
        self.soldeId = soldeId
        self.tauxSolde = tauxSolde
        self.dateDebutSolde = dateDebutSolde
        self.dateFinSolde = dateFinSolde

    @classmethod
    @with_connection
    def select(cls,soldeId, **kwargs):
        # get cursor from connection in kwargs
        cursor = get_cursor(kwargs)

        # execute query
        query = "SELECT * FROM SOLDE WHERE SoldeId = %s "
        cursor.execute(query, (soldeId,))

        # instantiate one transaction from cursor
        soldes = []
        for solde in cursor:
            soldes.append(Solde(*solde))

        return soldes
    

    @classmethod
    @with_connection
    def select_all(cls, **kwargs):
        # get cursor from connection in kwargs
        cursor = get_cursor(kwargs)

        # execute query
        query = "SELECT * FROM SOLDE "
        cursor.execute(query)

         # instantiate all transactions from cursor
        soldes = []
        for solde in cursor:
            soldes.append(Solde(*solde))

        return soldes
    
    @classmethod
    @with_connection
    def insert(cls, solde, **kwargs):
        """
        Insert new solde
        :param: solde
        :return: the solde inserted
        """

        # get cursor from connection in kwargs
        cursor = get_cursor(kwargs)

        # execute query
        query = "INSERT INTO SOLDE (SoldeId, TauxSolde, DateDebutSolde, DateFinSolde) VALUES (%s, %s, %s, %s)"
        cursor.execute(query, (solde.soldeId, solde.tauxSolde, solde.dateDebutSolde, solde.dateFinSolde))

        return solde   
    
    @classmethod
    @with_connection
    def update(cls, solde, **kwargs):
        """
        Update the solde
        :param: solde
        :return: the solde updated
        """

        # get cursor from connection in kwargs
        cursor = get_cursor(kwargs)

        # execute query
        query = "UPDATE SOLDE SET TauxSolde = %s,DateDebutSolde = %s,DateFinSolde = %s WHERE SoldeId = %s"
        cursor.execute(query, (solde.tauxSolde,solde.dateDebutSolde,solde.dateFinSolde,solde.soldeId))

        return Solde(*cursor.fetchone())
    

    @classmethod
    @with_connection
    def delete(cls, solde, **kwargs):
        """
        Delete the solde
        :param: the id of the solde
        """

        # get cursor from connection in kwargs
        cursor = get_cursor(kwargs)

        # execute query
        query = "DELETE FROM SOLDE WHERE SoldeId = %s"
        cursor.execute(query, (solde))