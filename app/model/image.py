from app.database.connector import with_connection


class Image:
    def __init__(self, url=None ,alt=None, gameId=None ):
        self.url = url
        self.alt = alt
        self.gameId = gameId


    @classmethod
    @with_connection
    def select(cls,url, **kwargs):
        # get connection and cursor
        cnx = kwargs.pop("connection")
        cursor = cnx.cursor()

        # execute query
        query = "SELECT * FROM IMAGE_JEU WHERE URL_image = %s "
        cursor.execute(query, (url,))

         # instantiate all images from cursor
        images = []
        for image in cursor:
            images.append(Image(*image))

        return images
    

    @classmethod
    @with_connection
    def select_all(cls, **kwargs):
        # get connection and cursor
        cnx = kwargs.pop("connection")
        cursor = cnx.cursor()

        # execute query
        query = "SELECT * FROM IMAGE_JEU "
        cursor.execute(query)

         # instantiate all images from cursor
        images = []
        for image in cursor:
            images.append(Image(*image))

        return images
    
    @classmethod
    @with_connection
    def insert(cls, image, **kwargs):
        """
        Insert new image
        :param: image
        :return: the image inserted
        """

        # get connection and cursor
        cnx = kwargs.pop("connection")
        cursor = cnx.cursor()

        # execute query
        query = "INSERT INTO IMAGE_JEU (URL_image, Alt,Jeu) VALUES (%s, %s, %s)"
        cursor.execute(query, (image.url, image.alt,image.jeu ))

        return image

    @classmethod
    @with_connection
    def update(cls, image, **kwargs):
        """
        Update the image
        :param: image
        :return: the image updated
        """

        # get connection and cursor
        cnx = kwargs.pop("connection")
        cursor = cnx.cursor()

        # execute query
        query = "UPDATE IMAGE_JEU SET Alt = %s, Jeu = %s WHERE URL_image = %s"
        cursor.execute(query, (image.alt, image.jeu,image.url))

        return Image(*cursor.fetchone())
    

    @classmethod
    @with_connection
    def delete(cls, image, **kwargs):
        """
        Delete the image
        :param: the id of the image
        """

        # get connection and cursor
        cnx = kwargs.pop("connection")
        cursor = cnx.cursor()

        # execute query
        query = "DELETE FROM IMAGE_JEU WHERE URL_image = %s"
        cursor.execute(query, (image))
