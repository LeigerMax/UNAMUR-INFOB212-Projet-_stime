from app.model.objet_instance import ObjetInstance
from app.model.objet import Objet
from app.view.item_shop_details_view import item_shop_details_view



def item_shop_details(username,itemId, instance):

    if instance == 1:
        myObjet = ObjetInstance.select(itemId)
    else:
        myObjet = Objet.select(itemId)

    user_choice = item_shop_details_view()


