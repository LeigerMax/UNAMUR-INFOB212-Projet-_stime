from app.view.console_utils.colors import VIOLET
from app.view.console_utils.io import clear_console, color_print


def annual_sales_view(sales):

    clear_console()
    color_print("[ANNUAL SALES]", VIOLET)

    for sale in sales:
        print(f"{sale.annee} \t {sale.montant}€")

    print("\nPress enter to continue...")
    input()


def monthly_sales_view(sales):
    clear_console()
    color_print("[MONTHLY SALES]", VIOLET)

    for sale in sales:
        print(f"{sale.annee} - {sale.mois} \t {sale.montant}€")

    print("\nPress enter to continue...")
    input()

