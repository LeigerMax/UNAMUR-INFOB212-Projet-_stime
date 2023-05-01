from app.database.connector import with_connection

class Categorie:
    def __init__(self, nom=None, description=None):
        self.nom = nom
        self.description = description

    @classmethod
    @with_connection
    def select(cls, nom, **kwargs):
        """
        Get one categorie from
        :param nom: the name of the categorie to fetch
        :return: the categorie fetched
        """

        # get connection and cursor
        cnx = kwargs.pop("connection")
        cursor = cnx.cursor()
    
    @classmethod
    @with_connection
    def select_all(cls, **kwargs):
        """
        Get all users in the database
        :return: users fetched
        """

        # get connection and cursor
        cnx = kwargs.pop("connection")
        cursor = cnx.cursor()

        # execute query
        query = "SELECT * FROM CATEGORIE"
        cursor.execute(query)

        # instantiate all users from cursor
        categories = []
        for categorie in categories:
            categories.append(Categorie(*categorie))

        return categories
    
    @classmethod
    @with_connection
    def insert(cls, categorie, **kwargs):
        """
        Insert new categorie
        :param: categorie
        :return: the categorie inserted
        """

        # get connection and cursor
        cnx = kwargs.pop("connection")
        cursor = cnx.cursor()

        # execute query
        query = "INSERT INTO CATEGORIE (Nom, Description) VALUES (%s, %s)"
        cursor.execute(query, (categorie.nom, categorie.description))

        return Categorie(*cursor.fetchone())
    
    @classmethod
    @with_connection
    def update(cls, categorie, **kwargs):
        """
        Update the categorie
        :param: categorie
        :return: the categorie updated
        """

        # get connection and cursor
        cnx = kwargs.pop("connection")
        cursor = cnx.cursor()

        # execute query
        query = "UPDATE CATEGORIE SET Description = %s WHERE Nom = %s"
        cursor.execute(query, (categorie.description, categorie.nom))

        return Categorie(*cursor.fetchone())
    
    @classmethod
    @with_connection
    def delete(cls, id, **kwargs):
        """
        Delete the categorie
        :param: the id of the categorie
        """

        # get connection and cursor
        cnx = kwargs.pop("connection")
        cursor = cnx.cursor()

        # execute query
        query = "DELETE FROM CATEGORIE WHERE Nom = %s"
        cursor.execute(query, (id))