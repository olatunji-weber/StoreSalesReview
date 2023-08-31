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
    new_list = []
    for price in prices:
        new_list.append(price - reduce_by)
    return new_list

# prices = [30, 25, 40, 20, 20, 35, 45, 50, 35]
# last_week = [2, 3, 5, 8, 4, 4, 6, 2, 9]


def gross_revenue(sales_list):
    # calculate the total revenue generated from the products
    total = 0
    for i in range(len(prices)):
        total += prices[i] * last_week[i]
    return total


def average_daily_revenue():
    # calculate the average daily revenue generated from the products
    for i in range(len(products)):
        print(f"{products[i]} : {(prices[i] * last_week[i]) / 7}")


print(
    f"The Average of the prices of all products in the store is: {gross_average_price(prices)}")

print(f"The new price list is: {new_price_list(5)}")

print(f"The Total Sales is: {gross_revenue(last_week)}")

print("****" * 5)
print("****" * 5)
print()
print("The Average daily revenue generated from the products: ")
average_daily_revenue()
print()
print("****" * 5)
print("****" * 5)

# based on the new prices, which products are less than $ 30

new_list = new_price_list(5)
for i in range(len(new_list)):
    if new_list[i] < 30:
        print(f"Product {products[i]}'s new price is less than $30")
