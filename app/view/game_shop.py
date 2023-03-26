from app.view.console_utils.colors import BLUE
from app.view.console_utils.io import color_print, clear_console


def game_shop_view():
    clear_console()
    color_print("[STORE]", BLUE)
    print("\nPress enter to continue...")
