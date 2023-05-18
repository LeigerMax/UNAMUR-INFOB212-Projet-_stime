from app.controller.item_shop_platform import item_shop_platform
from app.controller.item_shop_users import item_shop_users
from app.view.item_shop import item_shop_view


def item_shop(username):

    user_choice = item_shop_view()

    match user_choice :
        case 1:
            item_shop_platform(username)
        case 2:
            item_shop_users(username)
        case 3:
            return

