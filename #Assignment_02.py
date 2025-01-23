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


    # Define the stock quantity for each product
    stock = {
        "Cheesecake": 18,
        "Kunafa": 15,
        "Coffee": 23,
        "Arabic Coffee": 20,
        "Matcha": 16,
        "Juice": 21,
        "Water": 30
    }


    order = []                     # Empty list will be filled during orders
    print("Welcome to the restaurant!")





    while True:                    # Continuous loop until the user decides to end the request                    
        display_menu(menu, stock)  # Display the menu available to the user.  
        choice = input("Enter the name of the item you want to order: ").strip()  # Request product selection from user 

        if choice in menu:          # Verify that the product is in the list
            if stock[choice] > 0:   # Check if the product is in stock
                while True:         # Inner ring to check the required quantity 
                    try:
                        quantity = int(input(f"How many {choice} would you like to order?: "))  
                        if quantity <= 0:
                            print("Quantity must be at least 1.")
                        
                         
                        