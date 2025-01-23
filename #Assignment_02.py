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
                        if quantity <= 0:                          # Verify that the entered quantity is valid.
                            print("Quantity must be at least 1.")  # Error message if quantity is incorrect
                        elif quantity > stock[choice]:             # Check if the required quantity is available in stock
                            print(f"Sorry, we only have {stock[choice]} {choice} available.")   # Message if the required quantity is more than stock
                        else:

                            stock[choice] -= quantity              # Reduce the quantity available in stock 
                            print(f"{quantity} {choice}(s) added to your order.")
                            break                                  # Exit the inner loop when the request succeeds



                    except ValueError:                      # Handling invalid entries
                        print("Invalid input. Please enter a valid number.")
            else:
                print(f"Sorry, {choice} is out of stock.")  # Message if product is not available
        else:
            print("Item not found in the menu. Please choose again.")  # Message if the product is not in the list


        # Check if the user wants to order more
        more = input("Do you want to order more? (yes/no): ").strip().lower()
        if more == "no":    # If the user decides not to order more
            break



    if not order:      # Check if the user did not request anything
        print("You did not order anything.")  
        return

    
    # Total order calculation
    total = calculate_total(order, menu)  
    print("\nYour Order:")
    for item, quantity in order:
        print(f"- {item} x{quantity}: {menu[item] * quantity} AED")  # View order details  
    print(f"Total: {total} AED")                                     # Print total


    while True:
        try:
            amount = float(input("Enter the amount you are paying: "))  # Enter payment amount
            if amount < total:                                          # Verify that the amount paid is sufficient
                print(f"Insufficient amount! You need {total - amount} AED more.")
            else:
                change = amount - total   # Remainder calculation
                print(f"Payment successful! Your change is {change:.2f} AED.")      # Payment Success Message

                # Show remaining quantities of products after payment
                print("\nRemaining stock after your order:")
                for item, quantity in order:
                    print(f"{item}: {stock[item]} units remaining")                 # Print remaining stock                 
                break

        except ValueError:  # Handling invalid entries
            print("Invalid input. Please enter a valid number.")

    print("Thank you for dining with us!")

                        
                         
                        