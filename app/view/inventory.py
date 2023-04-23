from app.view.console_utils.colors import BLUE
from app.view.console_utils.io import clear_console, color_print


def my_item_view(username):
    clear_console()
    color_print("[YOUR ITEMS]", BLUE)
    print("\nPress enter to continue...")
