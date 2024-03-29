from app.database.connector import with_connection, get_cursor


class Evaluation:
    def __init__(self, utilisateur=None, avis=None, approuve=None, username=None):
        self.utilisateur = utilisateur
        self.avis = avis
        self.approuve = approuve
        self.username = username
    
    @classmethod
    @with_connection
    def select(cls, utilisateur, avis, **kwargs):
        # get cursor from connection in kwargs
        cursor = get_cursor(kwargs)

        # execute query
        query = "SELECT * FROM EVALUATION WHERE Utilisateur = %s AND Avis = %s"
        cursor.execute(query, (utilisateur, avis))

        try:
            return Evaluation(*cursor.fetchone())
        except TypeError:
            return None
        

    @classmethod
    @with_connection
    def select_with_avisID(cls, avis, **kwargs):
        # get cursor from connection in kwargs
        cursor = get_cursor(kwargs)

        # execute query
        query = "SELECT E.*, U.username FROM EVALUATION E JOIN UTILISATEUR U ON E.utilisateur = U.UserId  WHERE Avis = %s"
        cursor.execute(query, (avis,))

        # instantiate all evaluations from cursor
        evaluations = []
        for evaluation in cursor.fetchall():
            evaluations.append(Evaluation(*evaluation))

        return evaluations

    @classmethod
    @with_connection
    def select_all(cls, **kwargs):
        # get cursor from connection in kwargs
        cursor = get_cursor(kwargs)

        # execute query
        query = "SELECT * FROM EVALUATION"
        cursor.execute(query)

        # instantiate all evaluations from cursor
        evaluations = []
        for evaluation in cursor.fetchall():
            evaluations.append(Evaluation(*evaluation))

        return evaluations

    @classmethod
    @with_connection
    def insert(cls, evaluation, **kwargs):
        # get cursor from connection in kwargs
        cursor = get_cursor(kwargs)

        # execute query
        query = "INSERT INTO EVALUATION (Utilisateur, Avis, Approuve) VALUES (%s, %s, %s)"
        cursor.execute(query, (evaluation.utilisateur, evaluation.avis, evaluation.approuve))

        return evaluation

    @classmethod
    @with_connection
    def update(cls, evaluation, **kwargs):
        # get cursor from connection in kwargs
        cursor = get_cursor(kwargs)

        # execute query
        query = "UPDATE EVALUATION SET Approuve = %s WHERE Utilisateur = %s AND Avis = %s"
        cursor.execute(query, (evaluation.approuve, evaluation.avis, evaluation.utilisateur))

        return evaluation

    @classmethod
    @with_connection
    def delete(cls, utilisateur, avis, **kwargs):
        # get cursor from connection in kwargs
        cursor = get_cursor(kwargs)

        # execute query
        query = "DELETE FROM EVALUATION WHERE Utilisateur = %s AND Avis = %s"
        cursor.execute(query, (utilisateur, avis))

        return cursor.rowcount > 0
