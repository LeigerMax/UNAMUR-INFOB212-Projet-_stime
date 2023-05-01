from app.database.connector import with_connection


class Avis:
    def __init__(self, avisId=None, gameId=None, auteur=None, date=None, note=None,commentaire=None):
        self.avisId = avisId
        self.gameId = gameId
        self.auteur = auteur
        self.date = date
        self.note = note
        self.commentaire = commentaire

    @classmethod
    @with_connection
    def select(cls,avisId, **kwargs):
        # get connection and cursor
        cnx = kwargs.pop("connection")
        cursor = cnx.cursor()

        # execute query
        query = "SELECT * FROM AVIS WHERE AvisId = %s "
        cursor.execute(query, (avisId,))

        # instantiate one adresse from cursor
        avis = []
        for avisI in cursor:
            avis.append(Avis(*avisI))

        return avis
    

    @classmethod
    @with_connection
    def select_all(cls, **kwargs):
        # get connection and cursor
        cnx = kwargs.pop("connection")
        cursor = cnx.cursor()

        # execute query
        query = "SELECT * FROM AVIS "
        cursor.execute(query)

         # instantiate all avis from cursor
        avis = []
        for avisI in cursor:
            avis.append(Avis(*avisI))

        return avis
    
    @classmethod
    @with_connection
    def insert(cls, avis, **kwargs):
        """
        Insert new avis
        :param: avis
        :return: the avis inserted
        """

        # get connection and cursor
        cnx = kwargs.pop("connection")
        cursor = cnx.cursor()

        # execute query
        query = "INSERT INTO AVIS (AvisId, Jeu,Auteur,Date,Note,Commentaire) VALUES (%s, %s, %s,%s, %s, %s)"
        cursor.execute(query, (avis.avisId, avis.jeu,avis.auteur,avis.date,avis.note,avis.commentaire))

        return avis
    
    @classmethod
    @with_connection
    def update(cls, avis, **kwargs):
        """
        Update the avis
        :param: avis
        :return: the avis updated
        """

        # get connection and cursor
        cnx = kwargs.pop("connection")
        cursor = cnx.cursor()

        # execute query
        query = "UPDATE AVIS SET Jeu = %s,Auteur = %s ,Date = %s ,Note = %s,Commentaire = %s WHERE AvisId = %s"
        cursor.execute(query, (avis.gameId,avis.auteur,avis.date,avis.note, avis.commentaire, avis.avisId))

        return Avis(*cursor.fetchone())
    
    @classmethod
    @with_connection
    def delete(cls, avis, **kwargs):
        """
        Delete the avis
        :param: the id of the avis
        """

        # get connection and cursor
        cnx = kwargs.pop("connection")
        cursor = cnx.cursor()

        # execute query
        query = "DELETE FROM AVIS WHERE AchatId = %s"
        cursor.execute(query, (avis))