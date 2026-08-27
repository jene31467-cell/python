# name = input("whats your name? ").strip().capitalize()
# if name:
#     print(f"Hello {name}")

# response = input("do you want to continue? ")
# if response in ["yes", "y"]:
#     print("continuing........")
# else:
#     print("stopping..........")


# Convert user input to boolean
# user_input = input("Enter 1 for true, 0 for false: ")
# try:
#     value = bool(int(user_input))
#     print(f"Boolean value: {value}")
# except ValueError:
#     print("Please enter 1 or 0!")

# Convert different types to strings
# print(str(42))
# print(str(3.14))
# print(str(True))
# print(str(None))
# print(str([1, 2, 3]))

# # Convert different values to booleans
# print(bool(0))
# print(bool(1))
# print(bool(""))
# print(bool("Hello"))
# print(bool([]))
# print(bool(None))

# Use str() to build a message
# name = "Alice"
# age = 30
# # message = "My name is " + name + " and I am " + str(age) + " years old."
# # print(message)

# # Better way
# print(f"My name is {name} and I am {age} years old.")


user_input = input("Enter a value: ")

print(f"Original: {user_input} (type: {type(user_input).__name__})")
print('='*40)

try:
    int_val = int(user_input)
    print(f"int: {int_val} (type: {type(int_val).__name__})")
except ValueError:
    print("int: Cannot convert")


try:
    float_val = float(user_input)
    print(f"float: {float_val} (type: {type(float_val).__name__})")
except ValueError:
    print("float: Cannot convert")