from app.model.adresse import Adresse
from app.model.utilisateur import Utilisateur
from app.view.console_utils.io import exit_stime
from app.view.profil import profil_delete_view, profil_edit_bill_adress_view, profil_edit_delivery_adress_view, profil_edit_email_view, profil_edit_firstname_view, profil_edit_lastname_view, profil_edit_password_view, profil_edit_view, profil_view


def profil(username):

    utilisateurId = Utilisateur.select_userid(username)
    data_user = Utilisateur.select(utilisateurId.user_id)
    data_user_instance = Utilisateur.select(user_id=utilisateurId.user_id)
    data_user_bill_adress = Adresse.select(data_user_instance.bill_address)
    data_user_delivery_adress = Adresse.select(data_user_instance.delivery_address)

    user_choice = profil_view(username,data_user,data_user_bill_adress,data_user_delivery_adress)

    match user_choice:
        case 1:
            data_user_edit = profil_edit_view(username,data_user,data_user_bill_adress,data_user_delivery_adress)
        
            match data_user_edit :
                case 1:
                    new_data = profil_edit_firstname_view(username)
                    data_user_instance.firstname = str(new_data)
                    Utilisateur.update(data_user_instance)

                    profil(username)

                case 2:
                    new_data = profil_edit_lastname_view(username)
                    data_user_instance.lastname = str(new_data)
                    Utilisateur.update(data_user_instance)

                    profil(username)

                case 3:
                    new_data = profil_edit_email_view(username)
                    data_user_instance.email = str(new_data)
                    Utilisateur.update(data_user_instance)

                    profil(username)

                case 4: 
                    new_data = profil_edit_password_view(username)
                    data_user_instance.password = str(new_data)
                    Utilisateur.update(data_user_instance)

                    profil(username)

                case 5:
                    new_data = profil_edit_bill_adress_view(username)
                    
                    # Récupération des informations d'utilisateur depuis la view
                    new_numero = new_data[0]
                    new_rue = new_data[1]
                    new_ville = new_data[2]
                    new_code_postal = new_data[3]
                    new_pays =new_data[4]
                    new_adress = Adresse.insert(Adresse(None,new_numero, new_rue, new_ville, new_code_postal, new_pays))

                    data_user_instance.bill_address = new_adress
                    Utilisateur.update(data_user_instance)
                    
                    profil(username)

                case 6:
                    new_data = profil_edit_delivery_adress_view(username)

                    # Récupération des informations d'utilisateur depuis la view
                    new_numero = new_data[0]
                    new_rue = new_data[1]
                    new_ville = new_data[2]
                    new_code_postal = new_data[3]
                    new_pays =new_data[4]
                    new_adress = Adresse.insert(Adresse(None,new_numero, new_rue, new_ville, new_code_postal, new_pays))

                    data_user_instance.delivery_address = new_adress
                    Utilisateur.update(data_user_instance)

                    profil(username)
                

                case 7:
                   profil(username)

            

        case 2:
            profil_delete_view(username,data_user)
            data_user_instance.firstname = " "
            data_user_instance.lastname = " "
            data_user_instance.email = " "
            data_user_instance.password = " "
            data_user_instance.inscription_date = "0000-01-01"
            data_user_instance.date_of_birth = "0000-01-01"
            data_user_instance.wallet = 0
            data_user_instance.bill_address = None
            data_user_instance.delivery_address = None
            Utilisateur.update(data_user_instance)
            exit_stime()
        case 3:
            return
  

