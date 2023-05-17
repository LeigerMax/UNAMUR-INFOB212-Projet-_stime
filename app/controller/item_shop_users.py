from app.controller.item_shop_details import item_shop_details
from app.model.transaction import Transaction
from app.view.item_shop_users import item_shop_users_view

def item_shop_users(username):
    all_transact = Transaction.select_all()

    user_choice = item_shop_users_view(all_transact)

    if user_choice==0:
        return
    else :
        item_shop_details(username,user_choice)

