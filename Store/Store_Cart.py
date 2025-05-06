class inventory:
    def __init__(self):
        self.items = {}
        self.name = ""
        self.location = ""
        print("Inventory initialized.")

    def set_store_info(self, name, location):
        self.name = name
        self.location = location

    def add_item(self, title, price):
        self.items[title] = price
        print(f"Item '{title}' added with price {price}.")

    def remove_item(self, title):
        if title in self.items:
            del self.items[title]
            print(f"Item '{title}' removed.")
        else:
            print(f"Item '{title}' not found in inventory.")

    def display_inventory(self):
        if not self.items:
            print("No items found in inventory.")
        else:
            print("-------------------")
            print("Products as follow:")
            for title, price in self.items.items():
                print(f"{title}: ${price:.2f}")

    def display_store(self):
        print(f"User placed order from: {self.name} at address: {self.location}")


class cart(inventory):
    def __init__(self):
        super().__init__()
        self.cart_items = {}
        self.total = 0.0

    def add_to_cart(self, item, qty):
        if item in self.items:
            if qty > 0:
                if item in self.cart_items:
                    self.cart_items[item] += qty
                else:
                    self.cart_items[item] = qty
                self.update_total()
            else:
                print("Invalid quantity.")
        else:
            print("Item not in inventory.")

    def remove_from_cart(self, item, qty):
        if item in self.cart_items:
            if qty <= self.cart_items[item]:
                self.cart_items[item] -= qty
                if self.cart_items[item] == 0:
                    del self.cart_items[item]
                self.update_total()
            else:
                print("Too much to remove.")
        else:
            print("Item not in cart.")

    def update_total(self):
        self.total = 0
        for i in self.cart_items:
            self.total += self.cart_items[i] * self.items[i]

    def show_cart(self):
        self.display_store()
        if not self.cart_items:
            print("Order in cart is : 0")
            print("---------------------")
        else:
            print("---------------------")
            print("Order in cart is :")
            for item in self.cart_items:
                print(item, "with quantity :", self.cart_items[item])
        print(f"Total receipt is $ {self.total:.2f}")


# --- Main Program ---
if __name__ == "__main__":
    my_cart = cart()
    my_cart.add_item("Milk", 2.50)
    my_cart.add_item("Bread", 1.98)
    my_cart.add_item("Egg", 0.70)
    my_cart.add_item("Flour", 1.18)
    my_cart.add_item("Oil", 4.00)
    my_cart.add_item("Cheese", 2.68)

    name = input("Which store would you like to order from?: ")
    location = input("Which location would you like to use?: ")
    my_cart.set_store_info(name, location)

    while True:
        my_cart.display_inventory()
        print("------------------------")
        item = input("What would you like?: ").title()
        try:
            qty = int(input("Enter quantity: "))
            my_cart.add_to_cart(item, qty)
        except:
            print("Invalid input.")
            continue

        my_cart.show_cart()
        remove = input("Would like to remove an item? (yes/no)?: ").lower()
        if remove == "yes":
            item = input("What item would you like to remove?: ").title()
            try:
                qty = int(input("How many would you like to remove?: "))
                my_cart.remove_from_cart(item, qty)
            except:
                print("Invalid amount.")
            my_cart.show_cart()

        more = input("Would you like to add another product (yes/no)?: ").lower()
        if more != "yes":
            break

    print("Thanks for shopping with us!")
