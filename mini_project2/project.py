
products = [
    {"id": 1, "name": "Laptop", "price": 45000},
    {"id": 2, "name": "Smartphone", "price": 15000},
    {"id": 3, "name": "Headphones", "price": 2000},
    {"id": 4, "name": "Keyboard", "price": 1200},
    {"id": 5, "name": "Mouse", "price": 800},
    {"id": 6, "name": "Charger", "price": 500},
    {"id": 7, "name": "USB Cable", "price": 300},
    {"id": 8, "name": "Backpack", "price": 2500}
]

cart = []

# 1. View Products
def view_products(products):
    print("\n=== Available Products ===")
    for product in products:
        print(f"ID: {product['id']}, Name: {product['name']}, Price: ₹{product['price']}")
    print()

# 2. Add to Cart
def add_to_cart(products, cart, product_id, quantity):
    cart_full = len(cart) >= 8 and not any(item["id"] == product_id for item in cart)
    if cart_full:
        print("Cart is full! Maximum 8 items allowed.")
    else:
        product_found = False
        for p in products:
            if p["id"] == product_id:
                product_found = True
                existing_item = None
                for item in cart:
                    if item["id"] == product_id:
                        existing_item = item
                        break
                if existing_item:
                    existing_item["quantity"] += quantity
                    print(f"Updated quantity for {existing_item['name']} to {existing_item['quantity']}.")
                else:
                    cart.append({
                        "id": p["id"],
                        "name": p["name"],
                        "price": p["price"],
                        "quantity": quantity
                    })
                    print(f"Added {quantity} x {p['name']} to cart.")
                break
        if not product_found:
            print("Invalid product ID.")

# 3. View Cart
def view_cart(cart):
    if not cart:
        print("\nCart is empty.\n")
    else:
        print("\n=== Your Cart ===")
        total = 0
        for item in cart:
            subtotal = item["price"] * item["quantity"]
            total += subtotal
            print(f"{item['name']} - ₹{item['price']} x {item['quantity']} = ₹{subtotal}")
        print(f"Total Amount: ₹{total}\n")

# 4. Update Cart
def update_cart(cart, product_id, quantity):
    found = False
    if quantity <= 0:
        print("Quantity must be at least 1.")
    else:
        for item in cart:
            if item["id"] == product_id:
                item["quantity"] = quantity
                print(f"Updated quantity for {item['name']} to {quantity}.")
                found = True
                break
        if not found:
            print("Product not found in cart.")

# 5. Remove from Cart
def remove_from_cart(cart, product_id):
    removed = False
    for item in cart:
        if item["id"] == product_id:
            cart.remove(item)
            print(f"Removed {item['name']} from cart.")
            removed = True
            break
    if not removed:
        print("Product not found in cart.")

# 6. Checkout
def checkout(cart):
    if not cart:
        print("\nCart is empty. Nothing to checkout.\n")
    else:
        print("\n=== Checkout ===")
        total = 0
        for item in cart:
            subtotal = item["price"] * item["quantity"]
            total += subtotal
            print(f"{item['name']} - ₹{item['price']} x {item['quantity']} = ₹{subtotal}")
        print(f"Total Bill: ₹{total}")
        print("Thank you for shopping with us!\n")
        cart.clear()

# 7. Menu
def menu():
    while True:
        print("===== Shopping Cart =====")
        print("1. View Products")
        print("2. Add to Cart")
        print("3. View Cart")
        print("4. Update Cart")
        print("5. Remove from Cart")
        print("6. Checkout")
        print("7. Exit")

        choice = input("Enter your choice (1-7): ").strip()

        if choice == '1':
            view_products(products)

        elif choice == '2':
            product_id_input = input("Enter Product ID to add: ").strip()
            quantity_input = input("Enter Quantity: ").strip()
            if product_id_input.isdigit() and quantity_input.isdigit():
                product_id = int(product_id_input)
                quantity = int(quantity_input)
                if quantity > 0:
                    add_to_cart(products, cart, product_id, quantity)
                else:
                    print("Quantity must be greater than 0.")
            else:
                print("Invalid input. Please enter numbers only.")

        elif choice == '3':
            view_cart(cart)

        elif choice == '4':
            product_id_input = input("Enter Product ID to update: ").strip()
            quantity_input = input("Enter new Quantity: ").strip()
            if product_id_input.isdigit() and quantity_input.isdigit():
                product_id = int(product_id_input)
                quantity = int(quantity_input)
                update_cart(cart, product_id, quantity)
            else:
                print("Invalid input. Please enter numbers only.")

        elif choice == '5':
            product_id_input = input("Enter Product ID to remove: ").strip()
            if product_id_input.isdigit():
                product_id = int(product_id_input)
                remove_from_cart(cart, product_id)
            else:
                print("Invalid input. Please enter numbers only.")

        elif choice == '6':
            checkout(cart)

        elif choice == '7':
            print("Exiting... Goodbye!")
            break

        else:
            print("Invalid choice. Please select a valid option.")
menu()
