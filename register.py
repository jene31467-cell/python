# def register_user(username, password, age, is_admin=True):
#     """Register a user with validation."""

#     #validate username

#     if not username or len(username) < 3:
#         return None, "username must be atleast 3 characters"

#     #validate password

#     if not password or len(password) < 6:
#         return None, "password must be atleast 6 characters"

#     #validate age
#     if type(age) not in [int, float] or age < 0:
#         return None, "age must be positive number"
#     #validaate is_admin
#     if type(is_admin) != bool:
#         return None, "is_admin must have True or False"

#     #all checks passed

#     user = {
#         "username": username,
#         "age": age,
#         "is_admin": is_admin
#     }
#     return user, "registration successful"

# #test the function

# result, message = register_user("may", "password123", 30, True)

# if result is not None:
#     print(f"Sucess: {message}")
#     print(f"User: {result}")
# else:
#     print(f"Error: {message}")


# age = 20
# income = 100000

# is_old_enough = age >= 18
# has_income = income > 0
# print(f"is old enough? {is_old_enough}")
# print(f"Has income? {has_income}")
# print(f"can apply? {is_old_enough and has_income}")

# def get_type(value):
#     return type(value).__name__

# print(get_type(42))
# print(get_type(3.14))
# print(get_type("Hello"))
# print(get_type(True))
# print(get_type(None))

# def safe_divide(a, b):
#     if b == 0:
#         return None
#     return a / b
# result = safe_divide(10, 2)
# if result is not None:
#     print(f"Result: {result}")
# else:

#     print("cannot divide by zero!")

#     result = safe_divide(10, 2)
#     if result is not None:
#         print(f"Result: {result}")
#     else:
#         print('cannot divide by zero') 

#         result = safe_divide(35, 0)
#         if result is not None:
#             print(f"Result: {result}")
#         else:
#             print("cannot divide by zero!")

# data = [42, 3.14, "hello", True, None]
# for item in data:
#     print(f'{item} is a {type(item).__name__}')

name = input("what's your name?"  )
age_input = input("how old are you?" )
student_input = input("Are you a student?" )

if type(name) == str and len(name) > 0:
    print(f"Name: {name} - OK")
else:
    print(f"Nmae: Invalid = must be a non-empty string")

    #validate age

    age = int(age_input)
    if age >= 0:
        print(f"Age: {age} - OK")
    else:
        print("Age: Invalid - must be positive")


student_input = student_input.lower()
if student_input in["yes","no"]:
        student= student_input == "yes"
        print(f"Student: {student}- OK")
else:
        print(f"Student status: Invalid - must be yes or no")