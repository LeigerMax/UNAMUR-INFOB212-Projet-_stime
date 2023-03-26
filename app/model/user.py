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
    def select(cls, user_id):
        pass

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
