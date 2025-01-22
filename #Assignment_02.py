#Assignment 02

#Define the menu function
def display_menu(menu):
    print("\nMenu:")  
    for item, price in menu.items():
        print(f"{item}: {price} AED")      # Show items with price


def calculate_total(order, menu):
    total = 0                 # Total starts from zero
    for item in order:       
        total += menu[item]  
    return total             

