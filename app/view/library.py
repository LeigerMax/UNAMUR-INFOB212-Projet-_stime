from app.view.console_utils.colors import BLUE
from app.view.console_utils.io import clear_console, color_print


def library_view(games):
    """
    Display games of the user in a beautiful array.
    :param games: the list of games to show
    """

    clear_console()
    color_print("[YOUR LIBRARY]", BLUE)

    if len(games) == 0:
        print("You don't have any games yet. You can visit the shop to buy new games.")
    else:
        print(f"You have {len(games)} game(s).\n")

        # Max length for game titles
        game_title_size = 0
        for game in games:
            if len(game[0]) > game_title_size:
                game_title_size = len(game[0])

        # Spaces before title
        space_before_title = 2

        # Total width
        total_width = (space_before_title * 2) + game_title_size

        # Top of the array
        print('|' + '-' * (total_width + 2) + '|')

        for game in games:
            game_title = game[0]
            padding_width = total_width - len(game_title) - (space_before_title * 2)
            padding = ' ' * padding_width
            print(f'|{" " * space_before_title}{game_title}{padding}{" " * space_before_title}  |')
            # Lower lines for the array
            print('|' + '-' * (total_width + 2) + '|')

    print("\nPress enter to continue...")
