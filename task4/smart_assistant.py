import random

def weather_advice(temp, condition=None):
    if condition == "rainy":
        return "It's raining - take an umbrella!"
    elif temp < 10:
        return "It's quite cold — wear a warm jacket!"
    elif 10 <= temp < 20:
        return "A bit chilly— wear a light sweater."
    elif 20 <= temp < 30:
        return "Nice weather — enjoy a walk outside!"
    else:
        return "It's hot — stay hydrated and avoid the sun!"

def daily_expenses(expense_list):
    if not expense_list:
        return "No expenses entered."
    total = sum(expense_list)
    average = total / len(expense_list)
    return f"Total = ₺{total:.2f} | Average = ₺{average:.2f}"

def water_reminder(hours):
    glasses = hours * 2
    return f"Drink {glasses} glasses of water today! 💧"

def prioritize_tasks(tasks):
    if not tasks:
        return "No tasks added."
    sorted_tasks = sorted(tasks)
    return f"To-Do List (Prioritized): {sorted_tasks}"

def random_quote():
    quotes = [
        "Success is the sum of small efforts repeated daily.",
        "Believe in yourself — you’re stronger than you think.",
        "Push yourself, because no one else will do it for you.",
        "Discipline is the bridge between goals and accomplishment.",
        "Every day is a chance to be better than yesterday."
    ]
    return random.choice(quotes)

def main():
    print("Welcome to Smart Daily Assistant 💡")
    print("-----------------------------------")
    print("1. Weather Advice:", weather_advice(15))
    print("2. Expense Summary:", daily_expenses([120, 450, 200, 330, 100]))
    print("3. Water Reminder:", water_reminder(4))
    print("4. To-Do List:", prioritize_tasks(["Exercise", "Attend class", "Finish report"]))
    print("5. Motivation for the day:", f"\"{random_quote()}\"")

if __name__ == "__main__":
    main()
