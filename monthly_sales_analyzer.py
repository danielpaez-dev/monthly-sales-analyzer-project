# Example data
sales_data = [
    {"day": 1, "product_a": 202, "product_b": 142, "product_c": 164},
    {"day": 2, "product_a": 206, "product_b": 121, "product_c": 338},
    {"day": 3, "product_a": 120, "product_b": 152, "product_c": 271},
    {"day": 4, "product_a": 174, "product_b": 137, "product_c": 266},
    {"day": 5, "product_a": 199, "product_b": 153, "product_c": 301},
    {"day": 6, "product_a": 230, "product_b": 199, "product_c": 202},
    {"day": 7, "product_a": 101, "product_b": 137, "product_c": 307},
    {"day": 8, "product_a": 137, "product_b": 179, "product_c": 341},
    {"day": 9, "product_a": 287, "product_b": 70, "product_c": 310},
    {"day": 10, "product_a": 157, "product_b": 71, "product_c": 238},
    {"day": 11, "product_a": 148, "product_b": 108, "product_c": 319},
    {"day": 12, "product_a": 287, "product_b": 64, "product_c": 339},
    {"day": 13, "product_a": 289, "product_b": 100, "product_c": 257},
    {"day": 14, "product_a": 154, "product_b": 113, "product_c": 280},
    {"day": 15, "product_a": 150, "product_b": 184, "product_c": 170},
    {"day": 16, "product_a": 172, "product_b": 67, "product_c": 281},
    {"day": 17, "product_a": 188, "product_b": 109, "product_c": 163},
    {"day": 18, "product_a": 108, "product_b": 139, "product_c": 202},
    {"day": 19, "product_a": 229, "product_b": 133, "product_c": 241},
    {"day": 20, "product_a": 210, "product_b": 57, "product_c": 324}
]

def total_sales_by_product(data, product_key):
    """Calculates the total sales of a specific product in 30 days."""
    total_sales_of_product_key = 0

    for sale in sales_data:
        if product_key:
            total_sales_of_product_key += sale[product_key]
    
    return total_sales_of_product_key


def average_daily_sales(data, product_key):
    """Calculates the average daily sales of a specific product."""
    total_sales_of_product_key = total_sales_by_product(data, product_key)

    average_daily_sales_of_producty_key = total_sales_of_product_key / len(data)

    return average_daily_sales_of_producty_key


def best_selling_day(data):
    """Finds the day with the highest total sales."""
    best_selling_day = {"day": 0, "sells": 0} # This only works if there is no day with equal total sales. In case it happens this will only get the first day with that amount of sales

    for selling_day in data:
        total_sales_per_day = selling_day["product_a"] + selling_day["product_b"] + selling_day["product_c"]
        if total_sales_per_day > best_selling_day["sells"]:
            best_selling_day["day"] = selling_day["day"]
            best_selling_day["sells"] = total_sales_per_day

    return best_selling_day["day"]


def days_above_threshold(data, product_key, threshold):
    """Counts how many days the sales of a product exceeded a given threshold."""

    days_above_threshold = 0

    for selling_day in sales_data:
        if selling_day[product_key] > threshold:
            days_above_threshold += 1

    return days_above_threshold


def top_product(data):
    """Determines which product had the highest total sales in 30 days."""

    total_product_sales = {}

    for selling_day in sales_data:
        for product, value in selling_day.items():
            if product != "day":
                total_product_sales[product] = total_product_sales.get(product, 0) + value

    top_product = max(total_product_sales, key=total_product_sales.get)
    return top_product[-1].upper()

def worst_product(data):
    """Determines which product had the lowers total sales in 30 days."""
    
    total_product_sales = {}

    for selling_day in sales_data:
        for product, value in selling_day.items():
            if product != "day":
                total_product_sales[product] = total_product_sales.get(product, 0) + value

    worst_product = min(total_product_sales, key=total_product_sales.get)
    return worst_product[-1].upper()


def sorted_by_sales_product(data):
    """Sort all the products by selling in descending order."""
    
    total_product_sales = {}

    for selling_day in sales_data:
        for product, value in selling_day.items():
            if product != "day":
                total_product_sales[product] = total_product_sales.get(product, 0) + value

    sorted_products = sorted(total_product_sales, key=total_product_sales.get)

    final_sorted_product_by_letter = ""

    for i in range(len(sorted_products)):
        final_sorted_product_by_letter += sorted_products[i][-1].upper()
        if i + 1 != len(sorted_products):
            final_sorted_product_by_letter += ", "

    return final_sorted_product_by_letter

def max_min_range_of_a_product(data, product_key):
    """Calculate the range (max - min) of the sales of a product."""

    product_sales = [day[product_key] for day in data]
    range_of_sales_by_product = max(product_sales) - min(product_sales)

    return range_of_sales_by_product

# Function tests
print("Total sales of product_a:", total_sales_by_product(sales_data, "product_a"))
print("Average daily sales of product_b:", average_daily_sales(sales_data, "product_b"))
print("Day with highest total sales:", best_selling_day(sales_data))
print("Days when product_c exceeded 300 sales:", days_above_threshold(sales_data, "product_c", 300))
print("Product with highest total sales:", top_product(sales_data))
print("Product with lowest total sales:", worst_product(sales_data))
print("Products sorted by sales in descending order:", sorted_by_sales_product(sales_data))
print("Range of sales of product_a:", max_min_range_of_a_product(sales_data, "product_a"))
