from app.database.connector import with_connection


class User:
    def __init__(self, user_id=None, username=None, password=None, firstname=None, lastname=None, email=None, date_of_birth=None, inscription_date=None):
        self.userid = user_id
        self.username = username
        self.password = password
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.date_of_birth = date_of_birth
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
    def check_user_login(cls, username,password, **kwargs):
        """
        Get one user from the database
        :param user_id: the id of the user to fetch
        :return: the user fetched
        """

        # get connection and cursor
        cnx = kwargs.pop("connection")
        cursor = cnx.cursor()

        # execute query
        query = "SELECT * FROM UTILISATEUR WHERE Username = %s AND MDP = %s"
        cursor.execute(query, (username,password))

        row = cursor.fetchone()
        if row:
            return username
        else:
            return None
    
    
    @classmethod
    @with_connection
    def insert_new_user(cls, username, password, firstname, lastname, email,date_of_birth,inscription_date, **kwargs):
        """
        Insert one user from the database
        :param user_id: the id of the user to fetch
        :return: the user fetched
        """

        # get connection and cursor
        cnx = kwargs.pop("connection")
        cursor = cnx.cursor()

        # execute query
        query = """INSERT INTO UTILISATEUR (UserId,Username, Prenom, Nom, Email, MDP, DateInscription, DateNaissance, Portefeuille) VALUES (%s,%s, %s, %s, %s, %s, %s, %s, %s)"""
        cursor.execute(query, (1, username, lastname, firstname, email, password, inscription_date, date_of_birth,0))
        #TODO delet UserID

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
