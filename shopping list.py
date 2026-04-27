import os

products = []
quantity = []
price = []

def clear():
    os.system('cls')

def commands():
    print(" You can use the following commands to create a shopping list: ")
    print(" add - Add a product to the list\n" \
    " delete - Remove a product from the list\n" \
    " look - View the list\n" \
    " exit - Exit the program")
    print("-----------------------------------------")

def showlist():
    for i in range(len(products)):
        print (f"Product: {products[i]}, Quantity: {quantity[i]}, Price: {price[i]}")

def totalPrice():
        total = 0
        for productPrice in price:
            total += productPrice
        
        print(f"Total price: {total}")
        return total
                

while True:
    clear()
    commands()
    command = input("Enter a command: ").lower()
    match command:
        case "add":
            clear()
            productName = str(input("Enter product name: "))
            products.append(productName)

            productQuantity = int(input("Enter quantity: "))
            quantity.append(productQuantity)

            productPrice = float(input("Enter price per unit/kg: "))
            
            if productQuantity > 1:

                productPrice *= productQuantity
                price.append(productPrice)

            else:

                price.append(productPrice)

            print("Product added to the list")
            input("Press any key to continue....")
            clear()

        case "look":

            clear()
            showlist()
            totalPrice()
            input("Press any key to continue....")
            clear()
        
        case "delete":
            clear()
            showlist()
            deleting = int(input("Delete item by its index (first item has index 0): "))
            del products[deleting]
            del quantity[deleting]
            del price[deleting]

            print("Product has been removed from the list.")
            input("Press any key to continue....")
            clear()

        case "exit":
            break



