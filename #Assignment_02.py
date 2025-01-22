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
