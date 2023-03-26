from app.database.connector import with_connection


class User:
    def __init__(self, user_id, username, password, firstname, lastname, birthdate, inscription_date):
        self.userid = user_id
        self.username = username
        self.password = password
        self.firstname = firstname
        self.lastname = lastname
        self.birthdate = birthdate
        self.inscription_date = inscription_date

    @classmethod
    @with_connection
    def select(cls, cnx, user_id):
        cursor = cnx.cursor()
        query = "SELECT * FROM users WHERE userid = %s"

        user = cursor.execute(query, (user_id,))
        cursor.close()

        return user

    @classmethod
    def select_all(cls):
        pass

    @classmethod
    def create(cls, user):
        pass

    @classmethod
    def update(cls, user):
        pass

    @classmethod
    def delete(cls, user):
        pass
