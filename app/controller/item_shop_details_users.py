from datetime import datetime
from app.model.objet import Objet
from app.model.objet_instance import ObjetInstance
from app.model.transaction import Transaction
from app.model.utilisateur import Utilisateur
from app.view.item_shop_details_view_user import item_shop_details_view_user



def item_shop_details_users(username,transactId):

    utilisateurId = Utilisateur.select_userid(username)
    myUser = Utilisateur.select(utilisateurId.user_id)
    myTransact = Transaction.select(transactId)
    myObjet = ObjetInstance.select(myTransact.objet)
    originalObject = Objet.select(myObjet.objet)

    user_choice = item_shop_details_view_user(myObjet, originalObject, 0, myTransact.prix_vente)

    if user_choice == 0:
        if myUser.wallet >= myTransact.prix_vente:
            ## retire argent
            myUser.wallet = myUser.wallet - myTransact.prix_vente
            Utilisateur.update(myUser)
            ##update transaction
            transact = Transaction.selectByObjInst(myObjet.id)
            transact.acheteur = myUser.user_id
            now = datetime.now()
            formatted_date = now.strftime('%Y-%m-%d')
            transact.date_vente = formatted_date
            Transaction.update(transact)
            ## donne argent
            vendeurId = transact.revendeur
            vendeur = Utilisateur.select(vendeurId)
            vendeur.wallet = vendeur.wallet + transact.prix_vente
            Utilisateur.update(vendeur)
            ## update objetInstance
            myObjet.date_obtention = formatted_date
            myObjet.possesseur = myUser.user_id
            ObjetInstance.update(myObjet)
        else:
            item_shop_details_view_user(myObjet, originalObject, 1, myTransact.prix_vente)
    else:
        return


