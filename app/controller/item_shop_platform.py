from app.controller.item_shop_details import item_shop_details
from app.model.objet import Objet
from app.view.item_shop_platform import item_shop_platform_view



def item_shop_platform(username):
    all_objet = Objet.select_all()

    user_choice = item_shop_platform_view(all_objet)

    if user_choice==0:
        return
    else :
        item_shop_details(username,user_choice,0)

