from app.controller.shop_panier import shop_panier
from app.model.objet import Objet
from app.model.objet_instance import ObjetInstance
from app.model.panier import Panier
from app.model.utilisateur import Utilisateur
from app.view.item_shop_details_view import item_shop_details_view



def item_shop_details_platform(username,itemId):

    utilisateurId = Utilisateur.select_userid(username)
    myObjet = Objet.select(itemId)

    user_choice = item_shop_details_view(myObjet)

    if user_choice == 0:
        panier_id = utilisateurId.user_id
        Panier.add_objetInstance(Panier(panier_id), ObjetInstance(itemId))
        objetI = ObjetInstance(None,None,None,itemId,panier_id)
        ObjetInstance.insert(objetI)
        shop_panier(username)
    else:
        return


