# score = 60
# submitted_project = True
# if score >= 90 and submitted_project:
#      print("A+")
# elif score >= 90:
#      print("A") 
# elif score >= 80:
#     print("B")
# elif score >= 70:
#     print("C")
# elif score >= 60 and submitted_project:
#     print("D")
# else:
#     print("F")

# score = 70
# submitted_project = False
# if score >= 90:
#     print("High score")
# else:
#     print("Low score")

# if submitted_project:
#     print("project is submitted")
# else:
#     print("project is not submitted")
# score = 88

# grade = "A" if score >= 90 else "F" if score >= 80 else "B"
# print(grade)

# email = 'ib@gmail.net'
# #clean string
# email = email.strip()
# if email == "":
#     print("email cannot be empty")

# elif not '@' in email and  '@' in email:
#     print("email is invalid must contain . and @")
# elif email.count('@') != 1:
#     print("email must contain only one @")
# elif not email.endswith(('.com', '.org', '.net')):
#     print('email must end with .com, .net, .org')

# elif len(email) > 254:
#     print("email is too long")
# elif not(email[0].isalnum() and email[-1].isalnum()):
#     print("email must start and end with alphanumeric characters")
# else:
#     print("email is valid")

password = input("enter password")
password = password.strip()
email = 'ib@gmail.com'

if password == "":
    print("password cannot be empty")
elif len(password) < 8:
    print("password must be atleast 8 character long")
elif not any(char.isupper() for char in password):
    print("password must contain atleast one uppercase letter")
elif not any(char.islower() for char in password):
    print("password must contain atleast one lowercase letter")
elif email == password:
    print("password cannot be same as email")
elif password[0].isalnum() and password[-1].isalnum():
    print("valid password")
else:
    print("password is valid")

