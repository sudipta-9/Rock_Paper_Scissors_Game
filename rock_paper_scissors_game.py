# Function to create a payment receipt
def create_payment_receipt():
    # Get user input
    customer_name = input("Enter customer name: ")
    date = input("Enter date (e.g., September 7, 2023): ")
    payment_method = input("Enter payment method: ")
    
    # Initialize an empty list for items
    items = []
    
    # Ask for items and their prices until the user is done
    while True:
        item_name = input("Enter item name (or 'done' to finish): ")
        if item_name.lower() == 'done':
            break
        item_price = float(input("Enter item price: $"))
        items.append((item_name, item_price))
    
    # Calculate the total amount
    total_amount = sum(item[1] for item in items)
    
    # Construct the receipt content
    receipt = f"Payment Receipt\n\n"
    receipt += f"Customer Name: {customer_name}\n"
    receipt += f"Date: {date}\n\n"
    
    # Add itemized list
    receipt += "Items:\n"
    for item_name, item_price in items:
        receipt += f"- {item_name}: ${item_price}\n"
    receipt += f"Total Amount: ${total_amount}\n\n"
    
    receipt += f"Payment Method: {payment_method}\n"
    
    # Print the receipt to the console
    print(receipt)
    
    # Save the receipt to a text file
    with open("payment_receipt.txt", "w") as file:
        file.write(receipt)

# Create a payment receipt
create_payment_receipt()
