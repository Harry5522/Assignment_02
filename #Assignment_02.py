#Assignment 02

# Show menu with prices
def display_menu(menu, stock):
    print("\nMenu:")
    for item, price in menu.items():
        print(f"{item}: {price} AED")     # Print product name and price


def calculate_total(order, menu):
    total = 0
    for item, quantity in order:
        total += menu[item] * quantity  
    return total  
