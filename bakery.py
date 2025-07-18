import os
import time
import sys


# Sweet Surrender Bakery Inventory Management

# Inventory structure: [ingredient_name, quantity, min_threshold]
inventory = [
    ["sugar", 10, 5],
    ["flour", 15, 8],
    ["salt", 5, 2]
]

def clear_screen():
# Clears the console screen.
    os.system('cls' if os.name == 'nt' else 'clear')


# Function to view current inventory
def view_inventory():
    print("\n--- Current Inventory ---")
    if not inventory:
        print("Inventory is empty.")
    else:
        for item in inventory:
            name, qty, min_thresh = item
            print(f"{name.title()}: {qty} units (Min: {min_thresh})")
            if qty < min_thresh:
                print("  ⚠️ Low stock warning!")

# Function to add a new ingredient
def add_ingredient():
    name = input("Enter ingredient name: ").lower()
    for item in inventory:
        if item[0] == name:
            print("Ingredient already exists.")
            return
    try:
        quantity = int(input("Enter quantity: "))
        threshold = int(input("Enter minimum stock threshold: "))
        inventory.append([name, quantity, threshold])
        print(f"{name.title()} added to inventory.")
    except ValueError:
        print("Please enter valid numbers.")

# Function to update stock levels
def update_stock():
    name = input("Enter ingredient name: ").lower()
    for item in inventory:
        if item[0] == name:
            try:
                change = int(input("Enter amount to add (or negative to subtract): "))
                item[1] += change
                print(f"{name.title()} updated. New quantity: {item[1]}")
                return
            except ValueError:
                print("Invalid input.")
                return
    print("Ingredient not found.")

# Function to search for an ingredient
def search_ingredient():
    name = input("Enter ingredient name to search: ").lower()
    for item in inventory:
        if item[0] == name:
            print(f"\n{name.title()} found:")
            print(f"Quantity: {item[1]}")
            print(f"Minimum Threshold: {item[2]}")
            if item[1] < item[2]:
                print("⚠️ Warning: Stock below minimum threshold!")
            return
    print("Ingredient not found.")

    # Function to set minimum stock threshold
    def set_threshold():
        name = input("Enter ingredient name: ").lower()
        for item in inventory:
            if item[0] == name:
                try:
                    threshold = int(input("Enter new minimum stock threshold: "))
                    item[2] = threshold
                    print(f"Minimum stock threshold updated for {name.title()}.")
                    return
                except ValueError:
                    print("Invalid input.")
                    return
        print("Ingredient not found.")

# Main program loop
def main():
    while True:
        print("\n=== Bakery Inventory Management ===")
        print("1. View Inventory")
        print("2. Add New Ingredient")
        print("3. Update Stock Levels")
        print("4. Search for Ingredient")
        print("5. Set Minimum Stock Threshold")
        print("6. Exit")
        choice = input("Choose an option (1-6): ")

        if choice == "1":
            view_inventory()
        elif choice == "2":
            add_ingredient()
        elif choice == "3":
            update_stock()
        elif choice == "4":
            search_ingredient()
        elif choice == "5":
            set_threshold()
        elif choice == "6":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

# Run the program
if __name__ == "__main__":
    main()