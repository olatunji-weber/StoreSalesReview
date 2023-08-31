# Data for use
products = ["Sankofa Foods", "Jamestown Coffee", "Bioko Chocolate", "Blue Skies Ice Cream",
            "Fair Afric Chocolate", "Kawa Moka Coffee", "Aphro Spirit", "Mensado Bissap", "Voltic"]
prices = [30, 25, 40, 20, 20, 35, 45, 50, 35]
last_week = [2, 3, 5, 8, 4, 4, 6, 2, 9]


def gross_average_price(price_list):
    # calculate the total price average for all products
    gross_price = 0
    for price in price_list:
        gross_price += price
    return gross_price / len(price_list)


def new_price_list(reduce_by):
    # create a new price list that reduces the old prices by $ 5
    pass


def gross_revenue():
    # calculate the total revenue generated from the products
    pass


def average_daily_revenue():
    # calculate the average daily revenue generated from the products
    pass

# based on the new prices, which products are less than $ 30
