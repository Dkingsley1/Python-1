# ============================
# Inventory Management System
# ============================

#Inventory list (each item is a dictionary)
inventory = []


def add_item():
    print("\n--- Add Item ---")
    name = input("Enter item name: ")
    price = float(input("Enter item price: "))
    quantity = int(input("enter item quantity: "))
    category = input("Enter item category: ")

    item = {
        "name": name,
        "price": price,
        "quantity": quantity,
        "category": category
    }
    inventory.append(item)
    print(f"{name} added to inventory.\n")

def update_item():
    print("\n--- Update Item ---")
    name = input("Enter name of the item to update: ")

    for item in inventory:
        if item["name"].lower() == name.lower():
            print("Item found. Leave field blank to keep current value.")

            new_price = input(f"New price (current {item['price']}): ")
            new_quantity = input(f"New quantity (current {item['quantity']}): ")
            new_category = input(f"New category (current {item['category']}): ")

            if new_price:
                item["price"] = float(new_price)
            if new_quantity:
                item["quantity"] = int(new_quantity)
            if new_category:
                item["cagegory"] = new_category

            print("Item updated.\n")
            return
    print("Item not found.\n")

def view_inventory():
    print("\n--- Inventory ---")
    if not inventory:
        print("Inventory is empty.\n")
        return

    for item in inventory:
        print(f"Name: {item['name']}")
        print(f"Price: {item['price']}")
        print(f"Quantity: {item['quantity']}")
        print(f"Category: {item['category']}")
        print("---------------------------")
    print()

def remove_item():
    print("\n--- Remove Item ---")
    name = input("enter the name of the item to remove: ")

    for item in inventory:
        if item["name"].lower() == name.lower():
            inventory.remove(item)
            print(f"{name} removed from inventory.\n")
            return

    print("Item not found.\n")

def search_by_category():
    print("\n--- Search by Category ---")
    category = input ("Enter category to search: ")

    found_items = [item for item in inventory if item["category"].lower() == category.lower()]

    if not found_items:
        print("No items found in this category.\n")
        return
    print("\nItems in category:", category)
    for item in found_items:
        print(f"Name: {item['name']}, Price: {item['price']}, Quantity: {item['quantity']}")
    print()

# =========================
# Main Program Loop
# =========================

def main():
    while True:
        print("===== Inventory Menu ======")
        print("1. Add Item")
        print("2. Update Item")
        print("3. View Inventory")
        print("4. Remove Item")
        print("5. Search by Category")
        print("6. Exit")

        choice = input("Choose an option (1-6): ")

        if choice == "1":
            add_item()
        elif choice == "2":
            update_item()
        elif choice == "3":
            view_inventory()
        elif choice == "4":
            remove_item()
        elif choice == "5":
            search_by_category()
        elif choice == "6":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid option. Try again.\n")


# Run the program
main()


