from datetime import datetime
from app.model.transaction import Transaction
from app.model.utilisateur import Utilisateur
from app.view.user_sell_details import user_sell_details_view


def user_sell_details(username , choice):
    user = Utilisateur.select_userid(username)
    user_choice = user_sell_details_view(username)

    if user_choice == 0:
        return
    else :
        now = datetime.now()
        formatted_date = now.strftime('%Y-%m-%d')
        myTransact = Transaction(None,formatted_date,None,user_choice,user.user_id,None,choice)
        Transaction.insert(myTransact)
