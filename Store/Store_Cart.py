# Store products and their prices
PRODUCTS = {
    "Milk": 2.50,
    "Bread": 1.98,
    "Egg": 0.70,
    "Flour": 1.18,
    "Oil": 4.00,
    "Cheese": 2.68
}

# Store class


class Store:
    def __init__(self, name="", location=""):
        self.name = name
        self.location = location

    def set_info(self, name, location):
        self.name = name
        self.location = location

    def show_info(self):
        print(f"\nYou're shopping at: {self.name} - {self.location}")

# Cart class that inherits from Store


class Cart(Store):
    def __init__(self):
        super().__init__()
        self.items = {}  # Holds product names and quantities
        self.total = 0.0

    def add_item(self, product, quantity):
        if product not in PRODUCTS:
            print("Sorry, we don't have that product.")
            return
        if quantity <= 0:
            print("Please enter a valid quantity greater than 0.")
            return

        self.items[product] = self.items.get(product, 0) + quantity
        self.update_total()

    def remove_item(self, product, quantity):
        if product not in self.items:
            print("That item is not in your cart.")
            return
        if quantity <= 0:
            print("Quantity must be greater than 0.")
            return
        if quantity > self.items[product]:
            print("You can't remove more than what you added.")
            return

        self.items[product] -= quantity
        if self.items[product] == 0:
            del self.items[product]

        self.update_total()

    def update_total(self):
        self.total = sum(PRODUCTS[p] * q for p, q in self.items.items())

    def show_cart(self):
        self.show_info()
        if not self.items:
            print("Your cart is empty.")
        else:
            print("Items in your cart:")
            for product, qty in self.items.items():
                print(f"- {product}: {qty}")
        print(f"Total: ${self.total:.2f}\n")

# Display available products


def show_products():
    print("\nAvailable products:")
    for name, price in PRODUCTS.items():
        print(f"{name}: ${price:.2f}")

# Get a valid product from user


def get_product():
    while True:
        product = input("Enter product name: ").title()
        if product in PRODUCTS:
            return product
        else:
            print("Sorry, that product is not available.")

# Get a valid quantity


def get_quantity():
    while True:
        try:
            qty = int(input("Enter quantity: "))
            if qty > 0:
                return qty
            else:
                print("Quantity must be more than 0.")
        except ValueError:
            print("Please enter a valid number.")

# Main program


def main():
    cart = Cart()

    print("Welcome to the grocery shopping app!")
    store_name = input("Enter store name: ")
    store_location = input("Enter store location: ")
    cart.set_info(store_name, store_location)

    while True:
        show_products()
        product = get_product()
        quantity = get_quantity()
        cart.add_item(product, quantity)
        cart.show_cart()

        choice = input("Do you want to remove an item? (yes/no): ").lower()
        if choice == "yes":
            product = get_product()
            quantity = get_quantity()
            cart.remove_item(product, quantity)
            cart.show_cart()

        another = input(
            "Do you want to add another product? (yes/no): ").lower()
        if another != "yes":
            break

    print("Thanks for shopping with us!")


main()
