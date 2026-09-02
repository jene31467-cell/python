# name = input("what is your name? ")
# age = input("how old are you? ")
# favorite_food = input("whats your favorite food? ")
# age = int(age)

# print(f"My name is {name}, and i'm {age} years old. I love {favorite_food}")

# age = int(input("How old are you? "))

# if age < 13: 
#     print("You are a child.")
# elif age < 17:
#     print("You are a teenager.")
# elif age < 59:
#     print("you are an adult.")
# else:
#     print("You are a senior.")
balance = 10000
account = int(input("Add your account number: "))
withdrawal = int(input("how much do you want to withdraw: "))
if withdrawal > balance:
    print("insufficient funds.")
elif withdrawal <= 0:
    print("invalid withdrawal amonut") 
remaining_balance = balance - withdrawal
    print(remaining_balance)
else:
    remaining_balance < 5000:
    print("you are running low on funds.") 

