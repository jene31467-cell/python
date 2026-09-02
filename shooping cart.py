#create a class Item. A python class acts like atemplate: whenever we create a produc, it gets its own name,price,item_id and available stock

class Item:
    def __init__(self, item_id: str, name: str, price: float, stock: int):
        self.item_id = item_id
        self.name = name
        self.price = price
        self.stock = stock

    def __repr__(self):
        #defines how the item looks when printed
        return f"{self.name} (${self.price:.2f})"

#try stage 1

# laptop = Item(item_id="P1", name="Laptop", price=999.99, stock=5)
# mouse = Item(item_id="P2", name= "Mouse", price=25.00, stock=10)

# print(laptop)
# print(f"Available stock: {laptop.stock}")

class ShoppingCart:
    #manages items added by the customer.
    def __init__(self, tax_rate: float = 0.08):
        self.items = {} #item_id: {'item': item, 'quantity': int}
        self.tax_rate = tax_rate
        self.discount = 0.0 #percentage discount (eg. 0.10 for 10%)

    def add_item(self, item: Item, quantity: int = 1):
        #adds an item to the cart or update quantity.
        if quantity <= 0:
            print("Add to cart! ")
            return
        if item.stock < quantity:
            print(f"Sorry, only {item.stock} unit(s) of {item.name} available.")
            return
        if item.item_id in self.items:
            self.iems[item.item_id]['quantity'] += quantity
        else:
            self.items[item.item_id] = {'item': item, 'quantity': quantity}
        item.stock -= quantity
        print(f"Added{quantity} * {item.name} to cart.")

    def remove_item(self, item_id: str, quantity: int = None):
        #removes an item or decreases its quantity
        if item_id not in self.items:
            print("Item not found in cart.")
            return

        cart_entry = self.items[item_id]
        if quantity is None or quantity >= cart_entry['quantity']:
            #return stock and delete from cart
            cart_entry['item'].stock += cart_entry['quantity']
            removed_name = cart_entry['item'].name
            del self.items[item_id]
            print(f"Removed all {removed_name} from cart.")
        else:
            cart_entry[quantity] -= quantity
            cart_entry['item'].stock += quantity
            print(f"Removed {quantity} * {cart_entry['item'].name} from cart.")

    def apply_discount(self, coupon_code: str):
        #applies simple coupon code.

        coupons = {"SAVE10": 0.10, "SAVE20": 0.20}
        if coupon_code in coupons:
            self.discount = coupons[coupon_code]
            print(f"Coupon '{coupon_code}' applied! ({int(self.discount * 100)}% off)")
        else:
            print("Invalid coupon code.")

    def calculate_subtotal(self) -> float:
        return sum(entry['item'].price * entry['quantity'] for entry in self.items.values())

    def calculate_total(self) -> float:
        subtotal = self.calculate_subtotal()
        discount_subtotal = subtotal * (1 - self.discount)
        tax = discount_subtotal * self.tax_rate
        return discount_subtotal + tax

    def display_receipts(self):
        #prints a styled checkout receipts.
        if not self.items:
            print("\nYour cart is empty!")
            return
        print("\n" + "=" * 40)
        print("             YOUR RECEIPT            ")
        print("="*40)

        for entry in self.items.values():
            item = entry['item']
            qty = entry['quantity']
            total_price = item.price * qty
            print(f"{item.name:<20} * {qty:<3} ${total_price:>7.2f}")
        subtotal = self.calculate_subtotal()
        print("-"*40)
        print(f"{'Subtotal:':<25} ${subtotal:>8.2f}")


        if self.discount > 0:
            discount_amount = subtotal * self.discount
            print(f"{'Discount (' + str(int(self.discount * 100)) + '%):':<25} -${discount_amount:>7.2f}")

        tax = (subtotal * (1 - self.discount)) * self.tax_rate
        print(f"{'Tax ('+ str(int(self.tax_rate * 100)) + '%):':<25} ${tax:>8.2f}")
        print("="* 40)
        print(f"{'GRAND TOTAL:':<25} ${self.calculate_total():>8.2f}")
        print("="* 40 + "\n")

#example usage

if __name__ == "__main__":
    # Create inventory
    laptop = Item("P001", "Gaming Laptop", 1200.00, stock=5)
    mouse = Item("P002", "Wireless Mouse", 25.50, stock=20)
    keyboard = Item("P003", "Mechanical Keyboard", 80.00, stock=10)

    # Initialize cart (8% tax rate)
    cart = ShoppingCart(tax_rate=0.08)

    # Add items
    cart.add_item(laptop, 1)
    cart.add_item(mouse, 2)
    cart.add_item(keyboard, 1)

    # Apply promo
    cart.apply_discount("SAVE10")

    # Display receipt
    cart.display_receipts()