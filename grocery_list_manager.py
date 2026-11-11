
# CGS2060 - Grocery Shopping List Manager
# A menu-driven application for managing grocery items and prices.

# Global lists
GROCERY_LIST = ["milk", "bread", "pineapple", "eggs", "skittles"]
ITEM_PRICES = [4.75, 3.50, 2.67, 7.99, 2.97]


def show_menu():
    """Display the available grocery list options."""
    print("\nPlease Select Your Desired Option:")
    print("1. View Grocery List")
    print("2. Add Item")
    print("3. Remove Item")
    print("4. Clear List")
    print("5. Show Total")
    print("6. Insert an Item")
    print("7. Remove Last Item")
    print("8. Find an Item")
    print("9. Split and Add Items")
    print("10. Exit")


def get_item_name(prompt):
    """Get a non-empty item name from the user."""
    while True:
        item = input(prompt).strip().lower()

        if item:
            return item

        print("Item name cannot be empty. Please try again.")


def get_price(prompt):
    """Get a valid, non-negative price from the user."""
    while True:
        try:
            price = float(input(prompt))

            if price >= 0:
                return price

            print("Price cannot be negative.")

        except ValueError:
            print("Please enter a valid number.")


def view_list():
    """Display all grocery items and their prices."""
    if not GROCERY_LIST:
        print("\nYour grocery list is empty!")
        return

    print("\nHere Is Your Grocery List:")

    position = 0

    for item in GROCERY_LIST:
        print(f"{position + 1}. {item.title()} - ${ITEM_PRICES[position]:.2f}")
        position += 1


def add_item():
    """Add a new grocery item and its price."""
    item = get_item_name("Please Enter Your Desired Item: ")
    price = get_price("Please Enter the Price for This Item: $")

    GROCERY_LIST.append(item)
    ITEM_PRICES.append(price)

    print(f"{item.title()} has been added to your grocery list!")


def remove_item():
    """Remove a grocery item and its corresponding price."""
    if not GROCERY_LIST:
        print("\nYour grocery list is empty!")
        return

    item = get_item_name("\nPlease Enter the Item You Wish to Remove: ")

    if item in GROCERY_LIST:
        position = GROCERY_LIST.index(item)

        GROCERY_LIST.remove(item)
        ITEM_PRICES.pop(position)

        print(f"{item.title()} has been removed!")
    else:
        print(f"{item.title()} is not in your grocery list!")


def clear_list():
    """Clear all grocery items and prices after confirmation."""
    if not GROCERY_LIST:
        print("\nYour grocery list is already empty!")
        return

    confirm = input(
        "\nAre You Sure You Want to Clear Your Entire Grocery List? "
        "(yes or no): "
    ).strip().lower()

    if confirm == "yes":
        GROCERY_LIST.clear()
        ITEM_PRICES.clear()
        print("Your grocery list has been cleared!")
    else:
        print("Clear option canceled.")


def show_total():
    """Calculate and display grocery cost information."""
    if not GROCERY_LIST:
        print("\nYour grocery list is empty!")
        return

    total = sum(ITEM_PRICES)
    cheapest = min(ITEM_PRICES)
    most_expensive = max(ITEM_PRICES)

    print("\nGrocery List Calculations")
    print("-------------------------")
    print(f"Total Cost: ${total:.2f}")
    print(f"Cheapest Item: ${cheapest:.2f}")
    print(f"Most Expensive Item: ${most_expensive:.2f}")
    print(f"Total Number of Items: {len(GROCERY_LIST)}")


def insert_item():
    """Insert a grocery item and price at a chosen position."""
    item = get_item_name("Please Enter the Item You Wish to Insert: ")
    price = get_price("Please Enter the Price of Your Item: $")

    while True:
        try:
            position = int(
                input(f"Enter a Position (1-{len(GROCERY_LIST) + 1}): ")
            ) - 1

            if 0 <= position <= len(GROCERY_LIST):
                GROCERY_LIST.insert(position, item)
                ITEM_PRICES.insert(position, price)

                print(
                    f"{item.title()} has been inserted at "
                    f"position {position + 1}!"
                )
                return

            print("Invalid position. Please try again.")

        except ValueError:
            print("Please enter a whole number.")


def pop_item():
    """Remove the last grocery item and its price."""
    if not GROCERY_LIST:
        print("\nYour grocery list is empty!")
        return

    confirm = input(
        "Are You Sure You Want to Remove Your Last Item? "
        "(yes or no): "
    ).strip().lower()

    if confirm == "yes":
        popped_item = GROCERY_LIST.pop()
        ITEM_PRICES.pop()

        print(f"{popped_item.title()} has been removed!")
    else:
        print("Removal canceled.")


def find_item():
    """Find a grocery item and display its position and price."""
    if not GROCERY_LIST:
        print("\nYour grocery list is empty!")
        return

    item = get_item_name("Please Enter the Item You Wish to Find: ")

    if item in GROCERY_LIST:
        position = GROCERY_LIST.index(item)

        print(
            f"{item.title()} was found at position {position + 1}. "
            f"Price: ${ITEM_PRICES[position]:.2f}"
        )
    else:
        print(f"{item.title()} was not found in your grocery list!")


def split_items():
    """Split comma-separated input and add items with individual prices."""
    text = input(
        "Enter Comma-Separated Grocery Items: "
    ).strip()

    new_items = [
        item.strip().lower()
        for item in text.split(",")
        if item.strip()
    ]

    if not new_items:
        print("No valid items were entered.")
        return

    print(f"\nItems to Add: {new_items}")

    for item in new_items:
        price = get_price(f"Enter the price for {item.title()}: $")

        GROCERY_LIST.append(item)
        ITEM_PRICES.append(price)

    print(f"\n{len(new_items)} item(s) have been added!")


def main():
    """Run the grocery shopping list application."""
    print("*** Welcome to CGS2060 Grocery Shopping List Manager ***")

    keep_running = True

    while keep_running:
        show_menu()
        choice = input("\nYour Choice Is: ").strip().lower()

        match choice:
            case "1" | "view":
                view_list()

            case "2" | "add":
                add_item()

            case "3" | "remove":
                remove_item()

            case "4" | "clear":
                clear_list()

            case "5" | "total":
                show_total()

            case "6" | "insert":
                insert_item()

            case "7" | "last":
                pop_item()

            case "8" | "find":
                find_item()

            case "9" | "split":
                split_items()

            case "10" | "exit":
                print("\nThanks for Using Grocery Shopping List Manager!")
                keep_running = False

            case _:
                print("Invalid option! Please try again.")


# Start the program
if __name__ == "__main__":
    main()
