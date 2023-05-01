from app.database.connector import with_connection


class Evaluation:
    def __init__(self, utilisateur=None,avis=None, approuve=None):
        self.utilisateur = utilisateur
        self.avis = avis
        self.approuve = approuve
    
    @classmethod
    @with_connection
    def select(cls,utilisateur,avis, **kwargs):
        # get connection and cursor
        cnx = kwargs.pop("connection")
        cursor = cnx.cursor()

        # execute query
        query = "SELECT * FROM EVALUATION WHERE Utilisateur = %s AND Avis = %s "
        cursor.execute(query, (utilisateur,avis))

        # instantiate one evaluation from cursor
        evaluations = []
        for evaluation in cursor:
            evaluations.append(Evaluation(*evaluation))

        return evaluations
    

    @classmethod
    @with_connection
    def select_all(cls, **kwargs):
        # get connection and cursor
        cnx = kwargs.pop("connection")
        cursor = cnx.cursor()

        # execute query
        query = "SELECT * FROM EVALUATION "
        cursor.execute(query)

         # instantiate all evaluations from cursor
        evaluations = []
        for evaluation in cursor:
            evaluations.append(Evaluation(*evaluation))

        return evaluations
    

    @classmethod
    @with_connection
    def insert(cls, evaluation, **kwargs):
        """
        Insert new evaluation
        :param: evaluation
        :return: the evaluation inserted
        """

        # get connection and cursor
        cnx = kwargs.pop("connection")
        cursor = cnx.cursor()

        # execute query
        query = "INSERT INTO EVALUATION (Utilisateur, Avis, Approuve) VALUES (%s, %s, %s)"
        cursor.execute(query, (evaluation.utilisateur, evaluation.avis,evaluation.approuve ))

        return evaluation
    

    @classmethod
    @with_connection
    def update(cls, evaluation, **kwargs):
        """
        Update the evaluation
        :param: evaluation
        :return: the evaluation updated
        """

        # get connection and cursor
        cnx = kwargs.pop("connection")
        cursor = cnx.cursor()

        # execute query
        query = "UPDATE EVALUATION SET Approuve = %s WHERE Utilisateur = %s AND Avis = %s"
        cursor.execute(query, (evaluation.approuve, evaluation.avis,evaluation.utilisateur))

        return Evaluation(*cursor.fetchone())
    

    @classmethod
    @with_connection
    def delete(cls, utilisateur,avis, **kwargs):
        """
        Delete the evaluation
        :param: the utilisateur,avis of the evaluation
        """

        # get connection and cursor
        cnx = kwargs.pop("connection")
        cursor = cnx.cursor()

        # execute query
        query = "DELETE FROM EVALUATION WHERE Utilisateur = %s AND Avis = %s"
        cursor.execute(query, (utilisateur,avis))