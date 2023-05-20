from app.controller.item_shop_details_users import item_shop_details_users
from app.model.transaction import Transaction
from app.view.item_shop_users import item_shop_users_view

def item_shop_users(username):
    all_transact = Transaction.select_all_no_buy()

    transact_id = 0
    

    user_choice = item_shop_users_view(all_transact)

    for i, transact in enumerate(all_transact):
        if user_choice == i+1 :
            transact_id = transact.transaction_id

    if user_choice != 0 :
        item_shop_details_users(username,transact_id)
    else :
        return

