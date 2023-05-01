from app.database.connector import with_connection, get_cursor


class Image:
    def __init__(self, url=None, alt=None, game_id=None):
        self.url = url
        self.alt = alt
        self.game_id = game_id

    @classmethod
    @with_connection
    def select(cls, url, **kwargs):

        # get cursor from connection in kwargs
        cursor = get_cursor(kwargs)

        # execute query
        query = "SELECT * FROM IMAGE_JEU WHERE URL_image = %s"
        cursor.execute(query, (url))

        return Image(*cursor.fetchone())

    @classmethod
    @with_connection
    def select_all(cls, **kwargs):

        # get cursor from connection in kwargs
        cursor = get_cursor(kwargs)

        # execute query
        query = "SELECT * FROM IMAGE_JEU"
        cursor.execute(query)

        # instantiate all images from cursor
        images = []
        for image in cursor.fetchall():
            images.append(Image(*image))

        return images
    
    @classmethod
    @with_connection
    def insert(cls, image, **kwargs):

        # get cursor from connection in kwargs
        cursor = get_cursor(kwargs)

        # execute query
        query = "INSERT INTO IMAGE_JEU (URL_image, Alt, Jeu) VALUES (%s, %s, %s)"
        cursor.execute(query, (image.url, image.alt, image.jeu))

        return image

    @classmethod
    @with_connection
    def update(cls, image, **kwargs):

        # get cursor from connection in kwargs
        cursor = get_cursor(kwargs)

        # execute query
        query = "UPDATE IMAGE_JEU SET Alt = %s, Jeu = %s WHERE URL_image = %s"
        cursor.execute(query, (image.alt, image.jeu, image.url))

        return image

    @classmethod
    @with_connection
    def delete(cls, url, **kwargs):

        # get cursor from connection in kwargs
        cursor = get_cursor(kwargs)

        # execute query
        query = "DELETE FROM IMAGE_JEU WHERE URL_image = %s"
        cursor.execute(query, (url))

        return cursor.rowcount > 0
