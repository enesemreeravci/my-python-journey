from datetime import datetime
while True:
    print("=== Personal Expense Tracker ===")
    print("1. Add a new expense")
    print("2. View expenses for a specific date")
    print("3. View total spending (daily, weekly, monthly)")
    print("4. View summary by category")
    print("5. Save expenses")
    print("6. Load expenses")
    print("7. Exit")

    choice = int(input("Enter your choice: "))
    date_List = []
    spend_List = []
    category_List = []
    
    if(choice == 1):
        date = str(input("Enter the date (YYYY-MM-DD): "))
        description = str(input("Enter a description: "))
        amount = input("Enter the amount: ")
        category = input("Enter the category :")
        date_List.append(date)
        spend_List.append(amount)
        category_List.append(category)
    if(choice == 2):
        search_date = input("Date: ")
        total = 0
        for i in range(len(date_List)):
            if(date_List[i] == search_date):
                total += spend_List[i]
        if(total > 0):
            print("Total spending on {search_date}: {total}$")
        else:
            print("NO expenses found for this date")
    if(choice == 3):
        time_period = input('daily', 'weekly').strip().lower()
        if(time_period == "daily"):
            date = input("Enter date (YYYY-MM-DD): ").strip()
            p = datetime.strptime(time_period, "%y-%m-%d")
            total = sum(a for dt, a in zip(date_List, spend_List) if dt.time_period == p.date)
            print("Total spend on {d.date()}: {total} $")
        if(time_period == "weekly"):
             date = input("Enter any date in the month (YYYY-MM-DD): ").strip()
             d = datetime.strptime(date, "%Y-%m-%d")
             total = sum(a for dt, a in zip(date_List, spend_List)
                        if dt.year == d.year and dt.month == d.month)
             print(f"Total spent in {d.strftime('%B %Y')}: {total} USD")
        else:
            print("Invalid option. Please type 'daily', 'weekly', or 'monthly'.")

# continue