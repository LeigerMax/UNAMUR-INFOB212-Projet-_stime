
from app.model.v_entreprise import VEntreprise
from app.view.entreprise_profil_details import entreprise_profil_details_view


def entreprise_profil_details(username,entreprise):


    data_entreprise = VEntreprise.select(entreprise)
    

    entreprise_profil_details_view(data_entreprise)

    input()
    return
    
