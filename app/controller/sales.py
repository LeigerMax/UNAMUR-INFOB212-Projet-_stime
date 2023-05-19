from app.model.sales import Sales
from app.view.sales import annual_sales_view, monthly_sales_view


def annual_sales():
    # get annual sales from model
    sales = Sales.annual_sales()
    annual_sales_view(sales)


def monthly_sales():
    # get monthly sales from model
    sales = Sales.monthly_sales()
    monthly_sales_view(sales)
