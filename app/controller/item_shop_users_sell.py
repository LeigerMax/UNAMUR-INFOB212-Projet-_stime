from app.controller.item_shop_platform import item_shop_platform
from app.controller.item_shop_users import item_shop_users
from app.controller.user_sell_details import user_sell_details
from app.model.objet import Objet
from app.model.objet_instance import ObjetInstance
from app.model.utilisateur import Utilisateur
from app.view.item_shop_users_sell_view import item_shop_users_sell_view


def item_shop_users_sell(username):
    user = Utilisateur.select_userid(username)
    objectsInstance = ObjetInstance.select_all_from_user(user.user_id)
    objetsDatas = []
    for objet in objectsInstance:
        objetsDatas.append(Objet.select(objet.objet))

    user_choice = item_shop_users_sell_view(username,objectsInstance,objetsDatas)

    if user_choice != 0 :
        choiceId = 0
        for i, object in enumerate(objectsInstance):
            if user_choice == i+1 :
                choiceId = object.id

        user_sell_details(username, choiceId)
    else :
        return

