#Assignment 02


#Define the menu function
def display_menu(menu):
    print("\nMenu:")  
    for item, price in menu.items():
        print(f"{item}: {price} AED")      # Show items with price


def calculate_total(order, menu):
    total = 0                 # Total starts from zero
    for item in order:        # We go over each item in the
        total += menu[item]   # Add the item price to the total.
    return total              # Return the total value


def main():      # Menu with prices
           
    menu = {
        "Cheesecake": 35,
        "Kunafa": 30,
        "Coffee": 20,
        "Arabic Coffee": 25,
        "Matcha": 18,
        "Juice": 10,
        "Water": 4
    }


order = []          # Create an empty list to store orders
print("Welcome to the restaurant!")  


# Start the order process
while True:
    display_menu(menu)  # Show list
    choice = input("Enter the name of the item you want to order: ").strip()  # Enter the selection

# Verify that the item is in the list.
if choice in menu:
    order.append(choice)  # Add item to order
    print(f"{choice} added to your order.")  
else:
    print("Item not found in the menu. Please choose again.") # Error message when selecting a non-existent item


    more = input("Do you want to order more? (yes/no): ").strip().lower()
    if more == "np":
        break

