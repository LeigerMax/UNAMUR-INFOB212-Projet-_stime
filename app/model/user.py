from app.database.connector import with_connection, get_cursor


class User:
    def __init__(self, user_id=None, username=None, firstname=None, lastname=None, email=None, password=None,
                 inscription_date=None, date_of_birth=None, wallet=None, bill_address=None, delivery_address=None):
        self.user_id = user_id
        self.username = username
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.password = password
        self.inscription_date = inscription_date
        self.date_of_birth = date_of_birth
        self.wallet = wallet
        self.bill_address = bill_address
        self.delivery_address = delivery_address
    
    @classmethod
    @with_connection
    def select(cls, user_id, **kwargs):
        # get cursor from connection in kwargs
        cursor = get_cursor(kwargs)

        # execute query
        query = "SELECT * FROM user WHERE UserId = %s"
        cursor.execute(query, (user_id,))

        return User(*cursor.fetchone())
    
    @classmethod
    @with_connection
    def check_user_login(cls, username, password, **kwargs):
        # get cursor from connection in kwargs
        cursor = get_cursor(kwargs)

        # execute query
        query = "SELECT * FROM UTILISATEUR WHERE Username = %s AND MDP = %s"
        cursor.execute(query, (username, password))

        return User(*cursor.fetchone())
  
    @classmethod
    @with_connection
    def select_all(cls, **kwargs):
        # get cursor from connection in kwargs
        cursor = get_cursor(kwargs)

        # execute query
        query = "SELECT * FROM user"
        cursor.execute(query)

        # instantiate all users from cursor
        users = []
        for user in cursor.fetchall():
            users.append(User(*user))

        return users

    @classmethod
    @with_connection
    def create(cls, user, **kwargs):
        # get cursor from connection in kwargs
        cursor = get_cursor(kwargs)

        # execute query
        query = "INSERT INTO UTILISATEUR (Username, Prenom, Nom, Email, MDP, DateInscription, DateNaissance, Portefeuille) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        cursor.execute(query, (user.username, user.lastname, user.firstname, user.email, user.password, user.inscription_date, user.date_of_birth, 0))

        # store new id
        user.user_id = cursor.lastrowid

        return user

    @classmethod
    @with_connection
    def update(cls, user, **kwargs):
        # get cursor from connection in kwargs
        cursor = get_cursor(kwargs)

        # execute query
        query = "UPDATE UTILISATEUR SET Username = %s, Prenom = %s, Nom = %s, Email = %s, DateNaissance = %s, PorteFeuille = %s, AdresseLivraison = %s, AdresseFacturation = %s WHERE UserId = %s"
        cursor.execute(query, (user.username, user.lastname, user.firstname, user.email, user.password, user.inscription_date, user.date_of_birth, 0))

        return user

    @classmethod
    @with_connection
    def delete(cls, user_id, **kwargs):
        # get cursor from connection in kwargs
        cursor = get_cursor(kwargs)

        # execute query
        query = "DELETE FROM USER WHERE UserId = %s"
        cursor.execute(query, (user_id))

        return cursor.rowcount > 0
