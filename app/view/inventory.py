from app.view.console_utils.colors import BLUE, GREEN
from app.view.console_utils.io import clear_console, color_print


def my_item_view(username, myObjects, originalsObjects):
    clear_console()
    color_print("[YOUR ITEMS]", BLUE)
    for i, objet in enumerate(originalsObjects):
        color_print(f"{i} - {objet.nom} - {objet.description}", GREEN)
    print("\nPress enter to continue...")
