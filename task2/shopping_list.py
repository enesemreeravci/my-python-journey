
print("Welcome to the Grocery Shopping List Program!")

items = [] # to store our items

while True:
    print("\n") # I put extra line in ordr to increase readabletiy
    print("1. Add item")
    print("2. Remove item")
    print("3. View List")
    print("4. Total items")
    print("5. Exit")

    user_chocie = int(input("Choose an option: "))

    if(user_chocie == 1):
        item = input("Enter item to add: ")
        items.append(item)
        print("Item has added!")
    if(user_chocie == 2):
        item = input("Enter item to remove: ") # if there is no item to remove, program will give an error, i did not handle this case.
        items.remove(item)
        print("Item has removed!")
    if(user_chocie == 3):
        print("Your shopping list:\n ")
        print(items)
    if(user_chocie == 4):
        print("NUmber of items: ")
        print(len(items))
    if(user_chocie == 5):
        print("Byeeeee")
        break

