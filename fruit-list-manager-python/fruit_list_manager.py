# Fruit List Manager
# A simple beginner-friendly Python project to add, remove, and view fruits.

fruit_list = []

while True:
    print("\n--- Fruit List Manager ---")
    print("1. Add an item")
    print("2. Remove an item")
    print("3. Exit")

    try:
        user_option = int(input("Choose your option: "))
    except ValueError:
        print("Please enter a number: 1, 2, or 3.")
        continue

    if user_option == 1:
        item = input("Add an item to the list: ").strip()
        if item:
            fruit_list.append(item)
            print("Item added:", fruit_list)
        else:
            print("Item cannot be empty.")

    elif user_option == 2:
        item = input("Remove an item from the list: ").strip()
        if item in fruit_list:
            fruit_list.remove(item)
            print("Item removed:", fruit_list)
        else:
            print("Item not found in the list.")

    elif user_option == 3:
        print("Program closed. Goodbye!")
        break

    else:
        print("Invalid option. Please choose 1, 2, or 3.")
