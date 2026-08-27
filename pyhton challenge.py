name = input("enter name")
age =int(input("enter age"))

if name.strip() != "" and age >= 18:
    print("access granted")
else:
    print("access denied!")

password = input("enter password")

if len(password) >= 8 and "@"not in password:

    print("password invalid")
else:
    print("password valid")

email = input("enter email")
if email.strip() != "" and "@" in email and email.endswith(".com"):
    print("valid email")
else:
    print("invalid input")

if name is not None and isinstance(name, str) and len(name) > 5:
    print("valid username")
else:
    print("invalid username")

role = input("enter role- admin/moderator/user ").lower()
is_banned = input("is banned? yes/no: ").lower() == "yes"

is_verified = input("is verified? yes/no: ").lower() == "yes"

if (role == "admin" or role == "moderator") and (not is_banned or is_verified):
    print("access granted")
elif role == "user" and not is_banned and is_verified:
    print("access granted")
else:
    print("access denied")