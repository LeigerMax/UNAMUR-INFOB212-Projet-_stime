from app.database.connector import with_connection


class Image:
    def __init__(self, url=None ,alt=None ):
        self.url = url
        self.alt = alt


    @classmethod
    @with_connection
    def select(cls, **kwargs):
        """
        Get one image from the database
        :param user_id: the id of the user to fetch
        :return: the user fetched
        """

        # get connection and cursor
        cnx = kwargs.pop("connection")
        cursor = cnx.cursor()

        # execute query
        query = "SELECT * FROM IMAGE_JEU "
        cursor.execute(query)

        return 
    
