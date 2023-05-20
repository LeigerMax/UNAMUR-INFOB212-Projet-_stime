from app.model.objet import Objet
from app.model.objet_instance import ObjetInstance
from app.model.utilisateur import Utilisateur
from app.view.inventory import my_item_view


def my_item(username):

    user = Utilisateur.select_userid(username)
    objectsInstance = ObjetInstance.select_all_from_user(user.user_id)
    objetsDatas = []
    for objet in objectsInstance:
        objetsDatas.append(Objet.select(objet.objet))
    my_item_view(username, objectsInstance, objetsDatas)
    input()
