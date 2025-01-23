#Assignment 02

# Show menu with prices
def display_menu(menu, stock):
    print("\nMenu:")
    for item, price in menu.items():
        print(f"{item}: {price} AED")     # Print product name and price


def calculate_total(order, menu):
    total = 0               # Variable to save total
    for item, quantity in order:
        total += menu[item] * quantity  # Calculate the total cost of each product  
    return total 

# Main function to run the program
def main():

     # Definition of menu with product prices
    menu = {               
        "Cheesecake": 35,
        "Kunafa": 30,
        "Coffee": 20,
        "Arabic Coffee": 25,
        "Matcha": 18,
        "Juice": 10,
        "Water": 3
    } 
