# index = int(input("Which item do you want? "))
# items = ["apple", "banana", "orange"]
# print(items[index])


# try:
#     age = int(input("How old are you? "))
#     print(f"You are {age} years old.")
# except ValueError:   #error handling  
#     print("That's not a valid age!")



# try:
#     num1 = int(input("Enter the first number: "))
#     num2 = int(input("Enter the second number: "))
#     result = num1 + num2
#     print(f"{num1} + {num2} = {result}")
# except ValueError:    #error handling
#     print("Please enter valid numbers!")


# print(int("1234"))
# print(int(True))

# # Try to convert invalid input and handle the error
# try:
#     value = int(input("Enter a number: "))
#     print(f"You entered: {value}")
# except ValueError:
#     print("That's not a valid number!")

# while True:
#     user_input = input("ENter a number: ")
#     try:
#         number = int(user_input)
#         print(f"You entered: {number}")
#         print(f"Type: {type(number)}")
#         break
#     except ValueError:
#         print("That's not a valid number! ")


        # String to float
# print(float("3.14"))      # 3.14
# print(float("42"))        # 42.0
# print(float("-2.5"))      # -2.5
# print(float("1e-3"))      # 0.001 (scientific notation)

# # Integer to float
# print(float(10))          # 10.0
# print(float(-5))          # -5.0

# # Boolean to float
# print(float(True))        # 1.0
# print(float(False))       # 0.0

# Calculate area of a circle
# radius = float(input("Enter the radius: "))
# import math
# area = math.pi * radius ** 2
# print(f"Area: {area:.2f}")



#SHOPPING CART
# try:
#     price = float(input("Enter the price of the item: "))
#     quantity = float(input("Enter the quantity: "))
#     tax_rate = 0.0825

#     subtotal = price * quantity
#     tax = subtotal * tax_rate
#     total = subtotal + tax

#     print(f"Subtotal: ${subtotal:.2f}")
#     print(f"Tax: ${tax:.2f}")
#     print(f"Total: ${total:.2f}")
# except ValueError:
#     print("Please enter a valid number: ")


#BMI CALCULATOR

# try:
#     weight = float(input("ENter your weight in kg: "))
#     height = float(input("Enter your height in meters: "))

#     bmi = weight / (height ** 2)
#     print(f"Your bmi is: {bmi:.2f}")


#     if bmi < 18.5:
#         print("You're underweight. ")
#     elif bmi < 25:
#         print("You have a normal weight. ")
#     elif bmi < 30:
#         print("You are overweight ")
#     else:
#         print("Yo are obese. ")
# except ValueError:
#     print("Please enter valid numbers!") 

# Ask the user for a number and calculate its square
# value = float(input("Enter a number: "))
# square = value ** 2
# print(f"The square of {value} is {square:.2f}")


# # Try to convert invalid input and handle the error
# try:
#     value = float(input("Enter a number: "))
#     print(f"You entered: {value}")
# except ValueError:
#     print("That's not a valid number!")


# print("CURRENCY CONVERTER")
# print("="*20)

# try:
#     dollars = float(input("Enter amount in USD: "))
#     rate = float(input("Enter the conversion rate: "))

#     converted = dollars * rate

#     print(f"${dollars:.2f} USSD = {converted:.2f} at  rate {rate}")

# except ValueError:
#     print("pease enter a valid number")







#     # Try to convert invalid input and handle the error
# try:
#     value = float(input("Enter a number: "))
#     print(f"You entered: {value}")
# except ValueError:
#     print("That's not a valid number!")


price = 19.99
tax = 1.65
total = 21.64

# Without str()
print("Total: " + str(total))

# With formatting
print(f"Total: ${total:.2f}")