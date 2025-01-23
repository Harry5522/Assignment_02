#Assignment 02


def display_menu(menu, stock):
    print("\nMenu:")
    for item, price in menu.items():
        print(f"{item}: {price} AED")