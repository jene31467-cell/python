# order = "expresso"
# print(order[5:])
# name = input("what is your name? ")
# drink = input("What drink would you like to order? ")
# quantity = float(input("how many cups? "))
# price = quantity * 2.56
# receipt = f"order from {name}: {drink}-${price:.2f}"
# print(receipt)
# print(f"thank you, {name}! total: ${price:.2f}")

# sentence = "latte and expresso"
# words = sentence.split("and")
# print(words)
# rejoined = "-".join(words)
# print(rejoined)

# text = "apple banana orange mango"
# result = text.strip().lower()
# print(result)

# def greet_barista():
#     print("hello barista!... ")

# greet_barista()

# def order_drink(drink,size):
#     print('dispensing ' + size + ' ' + drink)

# order_drink('expresso', 'large')

# cups_ordered = 3
# price_per_cup = 4.50
# customer_receipt = ''

# def calculate_price(count, cost):
#     total = count * cost
#     return total 

# customer_receipt = calculate_price(cups_ordered,price_per_cup)
# print(customer_receipt)

# 
def order(drink, size = "medium", sugar=1):
    print(f'Drink: {drink}')
    print(f'Size: {size}')
    print(f'Sugar: {sugar}')

order('cream', 'large', 2)
order('expresso')
order(drink='coffee', sugar=3, size='extra large')