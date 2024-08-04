class ShoppingList:
    def __init__(self, item_name="none", item_price=0, item_quantity=0):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity

    def print_item_cost(self):
        total_cost = self.item_price * self.item_quantity
        print(f"{self.item_name} {self.item_quantity} @ ${self.item_price} = ${total_cost}")


class ShoppingCart:
    def __init__(self, customer_name="none", current_date="January 1, 2020"):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = []

    def add_item(self, item: ShoppingList):
        self.cart_items.append(item)

    def remove_item(self, item_name: str):
        found = False
        for item in self.cart_items:
            if item.item_name == item_name:
                self.cart_items.remove(item)
                found = True
                break
        if not found:
            print("There is no item in the cart. Nothing removed.")

    def modify_item(self, item: ShoppingList):
        found = False
        for cart_item in self.cart_items:
            if cart_item.item_name == item.item_name:
                if item.item_price != 0:
                    cart_item.item_price = item.item_price
                if item.item_quantity != 0:
                    cart_item.item_quantity = item.item_quantity
                found = True
                break
        if not found:
            print("Item not found in cart. Nothing modified.")

    def get_num_items_in_cart(self):
        total_quantity = sum(item.item_quantity for item in self.cart_items)
        return total_quantity

    def get_cost_of_cart(self):
        total_cost = sum(item.item_price * item.item_quantity for item in self.cart_items)
        return total_cost

    def print_total(self):
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        print(f"Number of Items: {self.get_num_items_in_cart()}")
        if not self.cart_items:
            print("Shopping Cart is Empty")
        else:
            for item in self.cart_items:
                item.print_item_cost()
            print(f"\nTotal: ${self.get_cost_of_cart()}")

    def print_descriptions(self):
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        print("Item Descriptions")
        if not self.cart_items:
            print("Shopping Cart is Empty ")
        else:
            for item in self.cart_items:
                print(f"{item.item_name}: {item.item_quantity} @ ${item.item_price}")

# Main function to implement the print_menu and interact with ShoppingCart class

def print_menu(cart: ShoppingCart):
    menu = """
MENU
a - Add item to cart
r - Remove item from cart
c - Change item quantity
i - Output items' descriptions
o - Output shopping cart
q - Quit
Choose an option: """
    option = ''
    while option != 'q':
        print(menu)
        option = input().lower()
        if option == 'a':
            print("Add item to cart")
            name = input("What is the item name: ")
            price = float(input("What is the item price: "))
            quantity = int(input("What is the item quantity: "))
            item = ShoppingList(name, price, quantity)
            cart.add_item(item)
        elif option == 'r':
            print("REMOVE ITEM FROM CART")
            name = input("Enter the item name to remove: ")
            cart.remove_item(name)
        elif option == 'c':
            print("CHANGE ITEM QUANTITY")
            name = input("Enter the item name: ")
            price = float(input("Enter the new price (0 if no change): "))
            quantity = int(input("Enter the new quantity (0 if no change): "))
            item = ShoppingList(name, price, quantity)
            cart.modify_item(item)
        elif option == 'i':
            print("OUTPUT ITEMS' DESCRIPTIONS")
            cart.print_descriptions()
        elif option == 'o':
            print("OUTPUT SHOPPING CART")
            cart.print_total()
        elif option == 'q':
            break
        else:
            print("Invalid option. Please choose again.")

# Example usage:

if __name__ == "__main__":
    customer_name = input("Enter customer's name: ")
    current_date = input("Enter today's date: ")
    cart = ShoppingCart(customer_name, current_date)
    print_menu(cart)
