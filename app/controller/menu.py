from app.controller.entreprise_profil import entreprise_profil
from app.controller.game_shop import game_shop
from app.controller.inventory import my_item
from app.controller.item_shop import item_shop
from app.controller.library import library
from app.controller.login import login
from app.controller.sales import annual_sales, monthly_sales
from app.controller.shop_panier import shop_panier
from app.controller.profil import profil
from app.controller.register import register
from app.view.console_utils.io import exit_stime
from app.view.menu import welcome_menu_view, utilisateur_menu_view, compta_menu_view
from database.roles import Roles


def welcome_menu():
    user_choice = welcome_menu_view()

    match user_choice:
        case 1:
            main_menu(register())
            exit_stime()
        case 2:
            main_menu(login())
        case 3:
            exit_stime()


def main_menu(user):
    username = user.username

    match user.role:
        case Roles.UTILISATEUR_ROLE:
            user_choice = utilisateur_menu_view(username)

            match user_choice:
                case 1:
                    library(username)
                    main_menu(user)
                case 2:
                    my_item(username)
                    main_menu(user)
                case 3:
                    game_shop(username)
                    main_menu(user)
                case 4:
                    item_shop(username)
                    main_menu(user)
                case 5:
                    shop_panier(username)
                    main_menu(user)
                case 6:
                    profil(username)
                    main_menu(user)
                case 7:
                    entreprise_profil(username)
                    main_menu(user)
                case 8:
                    exit_stime()
                    exit_stime() #TODO: remove duplicate and fix the bug !!

        case Roles.COMPTA_ROLE:
            user_choice = compta_menu_view(username)

            match user_choice:
                case 1:
                    annual_sales()
                    main_menu(user)
                case 2:
                    monthly_sales()
                    main_menu(user)
                case 3:
                    exit_stime()