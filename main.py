print("=== Shopping Cart Calculator ===")

products = {
    1: {"name": "Shoes", "price": 50.00},
    2: {"name": "Shirt", "price": 30.00},
    3: {"name": "Jeans", "price": 80.00},
    4: {"name": "Hat", "price": 20.00},
    5: {"name": "Bag", "price": 120.00}
}

def show_products():
    print("\n=== Available Products ===")
    for pid, item in products.items():
        print(f"{pid}. {item['name']} - RM{item['price']:.2f}")

def show_cart(cart):
    if not cart:
        print("\n Cart is empty.")
    else:
        print("\n=== Your Cart ===")
        for idx, item in enumerate(cart, start=1):
            print(f"{idx}. {item['name']} | RM{item['price']:.2f} × {item['quantity']} = RM{item['cost']:.2f}")

cart = []
total_cost = 0.0

while True:
    show_products()
    show_cart(cart)

    choice = input("\nEnter product ID to add, 'remove' to delete item, or 'done' to checkout: ")

    if choice.lower() == "done":
        break

    elif choice.lower() == "remove":
        if not cart:
            print(" Cart is empty, nothing to remove.")
            continue
        try:
            show_cart(cart)
            remove_id = int(input("Enter cart item number to remove: "))
            if 1 <= remove_id <= len(cart):
                removed_item = cart.pop(remove_id - 1)
                total_cost -= removed_item["cost"]
                print(f" Removed {removed_item['quantity']} x {removed_item['name']} from cart.")
            else:
                print(" Invalid item number.")
        except ValueError:
            print(" Please enter a valid number.")
        continue

    try:
        choice = int(choice)
        if choice not in products:
            print(" Invalid product ID. Try again.")
            continue

        quantity = int(input(f"Enter quantity for {products[choice]['name']}: "))
        if quantity <= 0:
            print(" Quantity must be more than 0.")
            continue

        # Calculate cost
        item = products[choice]
        cost = item["price"] * quantity

        # Add to cart
        cart.append({"name": item["name"], "price": item["price"], "quantity": quantity, "cost": cost})
        total_cost += cost

        print(f" Added {quantity} x {item['name']} (RM{item['price']:.2f} each) = RM{cost:.2f}")

    except ValueError:
        print(" Please enter a valid number.")

if total_cost > 0:
    show_cart(cart)
    print("\n=== Final Total ===")
    print(f" Total Price: RM{total_cost:.2f}")
else:
    print("\nNo items were purchased.")

