from prettytable import PrettyTable
import pyfiglet  # Font type

# Menus category
menus = {
    "Drinks Menu": [
        {"Serial number": "1", "name": "Pepsi", "price": 3, "stock": 10},
        {"Serial number": "2", "name": "Mango Juice", "price": 2, "stock": 10},
        {"Serial number": "3", "name": "Water", "price": 1, "stock": 20},
        {"Serial number": "4", "name": "Fanta", "price": 3, "stock": 10},
        {"Serial number": "5", "name": "Smoothie", "price": 5, "stock": 10},
    ],
    "Snacks Menu": [
        {"Serial number": "6", "name": "Toblerone Chocolate", "price": 2, "stock": 10},
        {"Serial number": "7", "name": "Dairy Milk Chocolate", "price": 2, "stock": 10},
        {"Serial number": "8", "name": "Pringles Chips", "price": 3, "stock": 20},
        {"Serial number": "9", "name": "Brownies", "price": 4, "stock": 10},
        {"Serial number": "10", "name": "Cup Cakes", "price": 2, "stock": 10},
    ],
    "Emergency Things Menu": [
        {"Serial number": "11", "name": "Bandage Packets", "price": 2, "stock": 20},
        {"Serial number": "12", "name": "Wipes", "price": 2, "stock": 20},
        {"Serial number": "13", "name": "Mask", "price": 3, "stock": 20},
        {"Serial number": "14", "name": "Ice Pack", "price": 2, "stock": 20},
        {"Serial number": "15", "name": "Cottons", "price": 1, "stock": 20},
    ],
}

# Display items from menus
def display_menu(menu):
    table = PrettyTable()
    table.field_names = ["Serial Number", "Name", "Price", "Stock"]
    for item in menu:
        table.add_row([item["Serial number"], item["name"], item["price"], item["stock"]])
    print(table)

# Find an item by serial number using functions
def find_item_by_serial(serial):   
    for category, items in menus.items():
        for item in items:
            if item["Serial number"] == serial:
                return item
    return None

# Recommend other items
def recommend_items(category, current_item):
    recommendations = [
        item for item in menus[category] if item["name"] != current_item["name"] and int(item["stock"]) > 0
    ]                           # This ! mark ensures that same iteam is not recommended again.
    if recommendations:
        print("\nWould you like to add something else:")
        display_menu(recommendations)
    else:
        print("\nNo other items to recommend in this category.")

# Payment Method and calculating change
def process_payment(item):
    while True:
        try:
            amount_paid = float(input(f"\nThe price is ${item['price']}. Please enter payment amount: $"))
            if amount_paid < item["price"]:
                print("Insufficient amount. Please pay at least the item price.")
            else:
                change = amount_paid - item["price"]
                print(f"Payment successful! Your change is ${change:.2f}.") # Change is rounded up to 2 decimal place.
                item["stock"] -= 1     
                return
        except ValueError:
            print("Invalid input. Please enter a valid amount.")

# Vending machine function
def vending_machine():
    welcome_msg = pyfiglet.figlet_format("WELCOME! to the Vending Machine") # Display a welcome messaage using aesthetic font.
    print(welcome_msg)
    
    while True:  # Allow multiple purchases
        # Display the menus
        for category, menu in menus.items():
            print(f"\n{category}")
            display_menu(menu)

        # Ask user for item selection
        serial = input("\nEnter the Serial Number of the item you want to purchase: ").strip() # To remove any extra spaces.
        item = find_item_by_serial(serial)

        if not item:
            print("Invalid Serial Number. Please try again.")
            continue

        if int(item["stock"]) <= 0:      
            print(f"Sorry, {item['name']} is out of stock.")  
            continue

        print(f"\nYou selected: {item['name']} - ${item['price']}")

        # Process payment
        process_payment(item)

        # Recommend other items in same category
        for category, items in menus.items():
            if item in items:
                recommend_items(category, item)
                break
            
        # Ask if the user wants to make another purchase
        another_purchase = input("\nWould you like to purchase another item? (yes/no): ").strip().lower() 
                                                                                       # to remove spaces and any capitalization.
        if another_purchase == "yes":
            continue  # Restart the loop for another purchase
        else:
            print("Thank you for using the vending machine. Have a great day!")
            break  # Exit the loop

if __name__ == "__main__":
    vending_machine()
    
