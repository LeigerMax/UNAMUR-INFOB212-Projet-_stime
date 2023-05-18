from app.controller.item_shop_details_platform import item_shop_details_platform
from app.model.objet import Objet
from app.view.item_shop_platform import item_shop_platform_view



def item_shop_platform(username):
    all_objet = Objet.select_all()

    user_choice = item_shop_platform_view(all_objet)

    if user_choice != 0 :
        item_shop_details_platform(username,user_choice)
    else :
        return

