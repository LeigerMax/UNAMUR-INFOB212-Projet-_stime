from app.database.connector import with_connection, get_cursor

class VEntreprise: 
    def __init__(self, nom=None, description=None, adresse_web=None, nom_jeu=None):
        self.nom = nom
        self.description = description
        self.adresse_web = adresse_web
        self.nom_jeu = nom_jeu


    @classmethod
    @with_connection
    def select(cls, nom, **kwargs):
        # get cursor from connection in kwargs
        cursor = get_cursor(kwargs)

        # execute query
        query = 'select * from vue_entreprise_jeux where Nom = "{}" '.format(nom)
        cursor.execute(query)

        # instantiate all transactions from cursor
        entreprises = []
        for entreprise in cursor.fetchall():
            entreprises.append(VEntreprise(*entreprise))

        return entreprises   

    @classmethod
    @with_connection
    def select_all(cls, **kwargs):
        # get cursor from connection in kwargs
        cursor = get_cursor(kwargs)

        # execute query
        query = "SELECT * FROM vue_entreprise_jeux"
        cursor.execute(query)

        # instantiate all transactions from cursor
        entreprises = []
        for entreprise in cursor.fetchall():
            entreprises.append(VEntreprise(*entreprise))

        return entreprises   