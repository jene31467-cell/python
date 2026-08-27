# name = input("what is your name? ")
# city = input("what city do you live in? ")
# hobby = input("what is your favorite hobby? ")

# print(f"\nHello, {name}! ")
# print(f"You live in {city}.")
# print(f"your favorite hobby is {hobby}")
# print(f"that's nice")

# name, age = input("enter name and age: ").split()

# age = int(age)
# print(f"Name: {name}, Age: {age}")

# name = input("what is your name?")
# if name == "":
#     print("you didn't enter anything! ")
# else:
#     print(f"Hello, {name}!")
# num1 = float(input("enter a first number: "))
# num2 = float(input("enter a second number: "))

# result = num1 + num2
# print(f"{result}")

# noun = input("enter a noun: ")
# verb = input('enter a verb: ')
# adjective = input('enter an adjective: ')
# place = input('enter a place: ')

# story = f"""
# One day, a {adjective} {noun} went to {place}.It wanted to {verb} all day long. Everyone was amazed by the {adjective} {noun} !
# """

# print(story)

# milk_ounce = 16
# pour_amount = 6
# remaining = milk_ounce - pour_amount
# print(remaining)

# cereal_in_box = 10
# required_scoops = 3
# print(cereal_in_box >= required_scoops)
# print(cereal_in_box <= required_scoops)
# print(cereal_in_box == required_scoops)
# print(cereal_in_box != required_scoops)

# is_milk_fresh = True
# is_cereal_fresh = False
# can_serve = is_milk_fresh and is_cereal_fresh
# print(can_serve)

# print(2+3*4)
# print((2+3)*4)
# ounce = 8.5
# print("pouring" + str(ounce) + "ounce of milk.")

# value1 = "15"
# value2 = 'banana'
# print(value1.isdigit())
# print(value2.isdigit())

# selected_drink = "coffee"
# target_temp = 100

# if selected_drink == 'green tea':
#     target_temp = 80
#     print('this line will be skipped')

#     print(target_temp)

# current_temperature = 100
# target_temperature = 70
# furnace_active = 'On'

# if current_temperature < target_temperature and occupancy_detected == True:
#     furncae_active = True
#     fan_speed = 'High'
# elif current_temperature < target_temperature - 5.0: 
#     furnace_active = True
#     fan_speed = 'emergency'
# else: 
#     furncae_active = False

#     print(furnace_active)
class User:
    def __init__(self, is_active, commission_rate):
        self.is_active = is_active
        self.commission_rate - commission_rate
def calculate_payout(user, amount):
    if user is not None:
        if user.is_active:
            if amount > 0:
                # Main "Happy Path" logic buried 3 tabs deep
                payout = amount * user.commission_rate
                return payout
            else:
                return "Invalid amount"
        else:
            return "Account inactive"
    else:
        return "No user found"

    test_user = User(is_active=True, comission_rate=0.15)
    print(calculate_payout(test_user, 100))