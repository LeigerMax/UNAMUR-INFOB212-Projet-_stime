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
    def select(cls, user_id, **kwargs):
        """
        Get one user from the database
        :param user_id: the id of the user to fetch
        :return: the user fetched
        """

        # get connection and cursor
        cnx = kwargs.pop("connection")
        cursor = cnx.cursor()

        # execute query
        query = "SELECT * FROM user WHERE userid = %s"
        cursor.execute(query, (user_id,))

        return User(*cursor.fetchone())

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
        query = "SELECT * FROM user"
        cursor.execute(query)

        # instantiate all users from cursor
        users = []
        for user in cursor:
            users.append(User(*user))

        return users

    @classmethod
    def create(cls, user):
        pass

    @classmethod
    def update(cls, user):
        pass

    @classmethod
    def delete(cls, user):
        pass
