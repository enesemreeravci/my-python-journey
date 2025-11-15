


sales_data = [
    [100, 150, 200, 250],
    [120, 160, 210, 240],
    [130, 170, 220, 260]
]

def print_total_sales_per_product():
    for i, row in enumerate(sales_data):
        total = sum(row)
        print(f"Product {i}: total sales: {total}")

while True:
    print("Welcome to the sales data analysis program!")
    print("-------------------------------------------")
    print("Total Sales per product:")
    # display  each product total sales
    print("Average Monthly Sales per Product: ")
    # display each product's average montly sales

    print("Total Sales per product:")
    # display each month's total sales

    print("Best-Selling product and Best Month: ")
    # indicate the best selling product and best month

    print("Sales trends analysis: ")
    # show sales trends for each product

    print("Forecast for Next Month ")
    # display forecasted   sales for each product