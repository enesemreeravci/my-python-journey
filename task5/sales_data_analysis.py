
sales_data = [
    [100, 150, 200, 250],
    [120, 160, 210, 240],
    [130, 170, 220, 260]
]

def print_total_sales_per_product():
    for i, row in enumerate(sales_data): # enumerate func allows us to loop through list, have access to both index and element itself
        total = sum(row)
        print(f"Product {i+1}: total sales: {total}")


def print_average_sales_per_product():
    for i, row in enumerate(sales_data):
        average = sum(row) / len(row)
        print(f"Product {i+1}: average sales: {average}")


def print_monthly_sales_per_product():
    for product_index, row in enumerate(sales_data):
        for month_index, value in enumerate(row):
            print(f"Product {product_index+1}: {month_index+1}.Month: {value}")


def print_best_sales_per_product():
    for i, row in enumerate(sales_data):
            best_sales = max(row)
            print(f"Product {i+1}: {best_sales} in month")  # I stucked here, but i am gonna figure it out :/

def print_analyze_sales_trends():
    for product_i, row in enumerate(sales_data):
        print(f"\nProduct {product_i+1}")
        for month_i, value in enumerate(row):
            print(f"  Month {month_i+1}: {value}")
        if row[-1] > row[0]:
            print("  Trend: Increasing")
        elif row[-1] < row[0]:
            print("Trend: Decreasing")
        else:
            print("Trend: Stable")

def print_forecast_for_next_month():
    for product_index, row in enumerate(sales_data):
        last_month = row[-1]
        previous_month = row[-2]
        growth = last_month - previous_month
        next_month = growth + last_month
        print(f"Product {product_index+1}: next month: {next_month}")
while True:
    print("Welcome to the sales data analysis program!")
    print("-------------------------------------------")
    print("Total Sales per product:")
    print_total_sales_per_product()
    print("Average Monthly Sales per Product: ")
    print_average_sales_per_product()
    print("Each Month's Total Sales per product:")
    print_monthly_sales_per_product()
    print("Best-Selling product and Best Month: ")
    print_best_sales_per_product()
    print("Sales trends analysis: ")
    print_analyze_sales_trends()
    print("Forecast for Next Month ")
    print_forecast_for_next_month()
    break
