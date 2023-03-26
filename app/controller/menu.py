from app.controller.game_shop import game_shop
from app.controller.inventory import my_item
from app.controller.item_shop import item_shop
from app.controller.library import library
from app.controller.login import login
from app.controller.register import register
from app.view.console_utils.io import exit_stime
from app.view.menu import welcome_menu_view, main_menu_view


def welcome_menu():
    user_choice = welcome_menu_view()

    match user_choice:
        case 1:
            main_menu(register())
        case 2:
            main_menu(login())
        case 3:
            exit_stime()


def main_menu(username):
    user_choice = main_menu_view(username)

    match user_choice:
        case 1:
            library(username)
            main_menu(username)
        case 2:
            game_shop()
            main_menu(username)
        case 3:
            item_shop()
            main_menu(username)
        case 4:
            my_item()
            main_menu(username)
        case 5:
            exit_stime()
